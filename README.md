# PythonFinalProject

**Slam algorithm with turtle bot and way point follower**

    • open terminal emulator in linux ubuntu 22.04 with ros2 and Nav2 pre installed 
    • Run the commands # ros2 launch turtlebot3_gazebo turtlebot3_my_world.launch.py 
    • My world is a coustom world created in gazebo 
    • run the command in the other terminal "ros2 launch turtlebot3_navigation2 
      navigation2.launch.py	 use_sim_time:=True map:=/home/shiva/maps/custom_map.yaml"
    • Note: You have to use the cyclone DDS processor 

**Wall Follower and obstacle avoidance :**

    • Clone the repo into your ros2 workspace 
    • Use colcon build select-packages -mobile_robo
    • Then launch the launch file using "ros2 launch mobile_robo mobile_robo_launch.py"

**System Perquisites**

    • Linux Ubuntu 22.04 
    • Ros2 humble 
    • Nav2 
    • Gazebo 
    • Rviz 
    • Visual studio code 
    • Cyclone DDS

![image](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/65ce038a-d478-40d5-b69d-ff1cf8e82567)

<p style="text-align: center;">Fig 1.1  Wall Following and Obstacle avoidance</p>

![Screenshot from 2023-04-30 22-36-25](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/c77ad981-579f-4081-8c3e-2028049b3e91)
                               Fig 1.2  Map in Rviz  

![proj_image](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/6a17d736-8ff0-4ae2-aaf9-170d60bec624)
                               Fig 1.3 Slam algorithm and waypoint Follower in Gazebo and Rviz 


