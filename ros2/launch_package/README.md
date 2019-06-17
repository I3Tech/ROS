# LAUNCH FILE
launch file is used to automatically launch one or more nodes from one or more packages

### How to run a launch file?
- add all the nodes in the order with which it should be launched along with its package name into the .launch.py file
- build the workspace (colcon build --symlink-install)
- set up the source to local bash (source <ros_ws_name>/install/local_setup.bash)
- launch all nodes with following command in the terminal: ros2 launch <launch_package_name> <launch_file_name>. In the example provided: ros2 launch launch sm.launch.py
