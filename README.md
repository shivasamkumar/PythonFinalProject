# PythonFinalProject

1. Clone the repo into your ros2 workspace 
2. Use colcon build select-packages -mobile_robo
3. Then launch the launch file using "ros2 launch mobile_robo mobile_robo_launch.py"


#The proj_workspace is a workspace which has slam algorithms in it , 
1. open terminal emulator in linux ubuntu 22.04 with ros2 and Nav2 pre installed 
2. Run the commands # ros2 launch turtlebot3_gazebo turtlebot3_my_world.launch.py 
3. My world is a coustom world created in gazebo 
4. run the command in the other terminal "ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=/home/shiva/maps/custom_map.yaml"

5.  Note: You have to use the cyclone DDS processor 

![proj_image](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/6a17d736-8ff0-4ae2-aaf9-170d60bec624)


![image](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/65ce038a-d478-40d5-b69d-ff1cf8e82567)
