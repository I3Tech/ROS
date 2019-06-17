# ROS imports
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        Node(package='test_pkg', node_executable='test_node', output='screen')
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
