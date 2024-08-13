
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_pkg',
            namespace='My_Node',
            executable='py_installed_exec',
            name='First_Node'
        ),
        Node(
            package='py_pkg',
            namespace='My_Topic',
            executable='py_exec_publisher',
            name='First_Publisher'
        ),
        Node(
            package='py_pkg',
            namespace='My_Topic',
            executable='py_exec_subscriber',
            name='First_Subscriber'
        ),
        Node(
            package='py_pkg',
            namespace='My_Service',
            executable='py_exec_server',
            name='First_Server'
        ),
        Node(
            package='py_pkg',
            namespace='My_Service',
            executable='py_exec_client',
            name='First_Client'
        ),
        Node(
            package='py_pkg',
            namespace='My_Action',
            executable='py_action_server',
            name='Action_Server'
        ),
        Node(
            package='py_pkg',
            namespace='My_Interface',
            executable='py_interface_pub',
            name='First_custom_Publisher'
        ),
        Node(
            package='py_pkg',
            namespace='My_Interface',
            executable='py_interface_sub',
            name='First_custom_Subscriber'
        )
    ])
