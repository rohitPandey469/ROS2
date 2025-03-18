import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')

        self.declare_parameter('topic', value="listener_topic")
        topic_name = self.get_parameter('topic').get_parameter_value().string_value

        self.subscription = self.create_subscription(
            String,
            topic_name,
            self.listener_callback, # This will be called everytime someone publishes to the topic
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)

    # Create a node
    listenerNode = ListenerNode()

    # Use node
    rclpy.spin(listenerNode)

    # Destroy node
    listenerNode.destroy_node()
    rclpy.shutdown() 

if __name__ == '__main__':
    main()