import os
import sys 
import time
import unittest
import uuid

import launch
import launch_ros
import launch_ros.actions
import launch_testing.actions

import rclpy
import std_msgs.msg

# Launch karna padega test node(or same node) 
def generate_test_description():
    file_path = os.path.dirname(__file__)
    talker_node = launch_ros.actions.Node(
        executable=sys.executable,
        arguments=[os.path.join(file_path,"..", "talker_listener", "talker_node.py")],
        additional_env={'PYTHONUNBUFFERED': '1'},
        parameters=[{
            "topic" : "talker_chatter"
        }]
    )

    listener_node = launch_ros.actions.Node(
        executable=sys.executable,
        arguments=[os.path.join(file_path,"..", "talker_listener", "listener_node.py")],
        additional_env={'PYTHONUNBUFFERED': '1'},
        parameters=[{
            "topic" : "listener_chatter"
        }]
    )
    return (
        launch.LaunchDescription([
        talker_node,
        listener_node,
        # Start test right away - no need to wait for anything
        launch_testing.actions.ReadyToTest()
        ]),
        {
            "talker": talker_node,
            "listener": listener_node
        }
    )


# Test Node
class TestTalkerListener(unittest.TestCase):
    # Test Interface Talker Node - Listener Node
    @classmethod
    def setUpClass(cls):
        # Inititalize the ROS context for the test node
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        # Shutdown the ROS context
        rclpy.shutdown()
    
    def setUp(self):
        # Create a ROS node for the test
        self.node = rclpy.create_node("test_talker_listener_link")

    def tearDown(self):
        self.node.destroy_node()

    def test_talker_transmits(self, talker, proc_output):
        msgs_rx = []
        # Create a subscriber to the talker chatter topic
        sub = self.node.create_subscription(std_msgs.msg.String, "talker_chatter", lambda msg: msgs_rx.append(msg), 10)
        
        try:
            # Wait until the talker transmits two messages over the ROS topic
            end_time = time.time() + 10.0
            while time.time() < end_time:
                rclpy.spin_once(self.node, timeout_sec=0.1)
                if len(msgs_rx) >= 2:
                    break

            self.assertGreater(len(msgs_rx), 1)

            # make sure the talker also output the same data via stdout
            for msg in msgs_rx:
                proc_output.assertWaitFor(
                    expected_output=msg.data, process=talker
                )

        finally:
            self.node.destroy_subscription(sub)

    def test_listener_receives(self, listener, proc_output):
        # Create a publisher to the listener chatter topic
        pub = self.node.create_publisher(std_msgs.msg.String, "listener_chatter", 10)

        time.sleep(2.0)
        try:
            msg = std_msgs.msg.String()
            msg.data = str(uuid.uuid4())

            for _ in range(10):
                pub.publish(msg)
                success = proc_output.waitFor(
                    expected_output=msg.data, process=listener, timeout=1.0
                )
                if success:
                    break

                assert success, "Waiting for the output timed out"
        finally:
            self.node.destroy_publisher(pub)