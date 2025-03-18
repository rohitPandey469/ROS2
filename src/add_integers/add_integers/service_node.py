import rclpy
from rclpy.node import Node
from custom_interfaces.srv import AddTwoInts

class AdditionService(Node):
    def __init__(self):
        super().__init__('add_int_service')
        self.service = self.create_service(
            AddTwoInts,
            'add_two_ints',
            self.add_two_ints_callback
        )

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f"Request: {request.a} + {request.b}")
        return response

def main(args=None):
    rclpy.init(args=args)

    # create node
    addition_service = AdditionService()

    # use/spin node
    rclpy.spin(addition_service)

    # destroy node
    addition_service.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
