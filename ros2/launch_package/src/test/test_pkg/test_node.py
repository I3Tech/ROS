
# ROS imports
import rclpy
from rclpy.node import Node

class StateMachine(Node):
    def __init__(self):
        super().__init__('test_node')
        self.get_logger().info('test node running')

def main(args=None):
    rclpy.init(args=args)
    test = StateMachine()

    rclpy.spin(test)
    print('\n test node shutting down \n')
    test.destroy_node()


if __name__ == '__main__':
    main()
