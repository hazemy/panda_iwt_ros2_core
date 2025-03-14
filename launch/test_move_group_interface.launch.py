from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("moveit_resources_panda").to_moveit_configs()

    # MoveGroupInterface demo executable
    move_group_demo = Node(
        name="test_move_group_interface",
        package="franka_fer1_ros2",
        executable="test_move_group",
        # package="panda_iwt_ros2_core",
        # name="panda_motion_controller_node",
        # executable="panda_main",
        output="screen",
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
        ],
    )

    return LaunchDescription([move_group_demo])
