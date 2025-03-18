import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')

        self.declare_parameter('topic', value="talker_topic")
        topic_name = self.get_parameter('topic').get_parameter_value().string_value

        self.publisher_ = self.create_publisher(String, topic_name, 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World! {self.count}'
        self.publisher_.publish(msg)
        self.count += 1
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)

    # Create a node
    talkerNode = TalkerNode()

    # Use Node
    rclpy.spin(talkerNode)

    # Destroy Node
    talkerNode.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()