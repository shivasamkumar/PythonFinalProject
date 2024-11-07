# PythonFinalProject

# Robot Car: Obstacle Avoidance and Wall Following with LiDAR

This project focuses on developing obstacle avoidance and wall-following algorithms using a LiDAR sensor mounted on a custom-built robot. Designed for navigation in a custom environment, the robot uses LiDAR data to detect and avoid obstacles and maintain a consistent distance from walls, enabling smooth and efficient navigation


## Installation

**Prequisites**

• Linux Ubuntu 22.04 

• Ros2 humble 

• Nav2 

• Gazebo 

• Rviz 

• Visual studio code 

• Cyclone DDS

**Step 1: Install ROS 2 Humble** 

Follow the [ROS 2 Humble installation](https://docs.ros.org/en/humble/Installation.html) instructions for your operating system if ROS 2 is not already installed.

**Step 2: Install Required ROS 2 Packages** 

Install the necessary ROS 2 packages.
```bash
sudo apt-get install ros-humble-ros2-control
sudo apt-get install ros-humble-ros2-controllers
sudo apt-get install ros-humble-xacro
sudo apt-get install ros-humble-ros-gz-*
sudo apt-get install ros-humble-*-ros2-control
sudo apt-get install ros-humble-joint-state-publisher-gui
sudo apt-get install ros-humble-turtlesim
sudo apt-get install ros-humble-robot-localization
sudo apt-get install ros-humble-joy-teleop
sudo apt-get install ros-humble-tf-transformations


```
**Step 3: Install Python Packages** 

Install Python and additional packages:
```bash
sudo apt-get install python3-pip
pip install transforms3d
```

## Run Locally

Clone the project

```bash
  git clone git@github.com:shivasamkumar/PythonFinalProject.git
```

Go to the project directory

```bash
  cd proj_wrkspace
```

build the project

```bash
  colcon build 
```

Source your workspace

```bash
  source /opt/ros/humble/setup.bash
  source ~/workspace/install/setup.bash 
```

Launch the project

**Slam algorithm with turtle bot and way point follower**

• open terminal emulator in linux ubuntu 22.04 with ros2 and Nav2 pre installed 

• Run the commands 

```bash
 ros2 launch turtlebot3_gazebo turtlebot3_my_world.launch.py 
  
```
• run the command in the other terminal 

```bash
  ros2 launch turtlebot3_navigation2 navigation2.launch.py	 use_sim_time:=True map:=/home/shiva/maps/custom_map.yaml"
```

---
**NOTE**

* Note: You have to use the cyclone DDS processor


---

**Wall Follower and obstacle avoidance**

```bash
• Clone the repo into your ros2 workspace 
• Use colcon build select-packages -mobile_robo
• Then launch the launch file using "ros2 launch mobile_robo mobile_robo_launch.py"

```



## Demo

![image](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/65ce038a-d478-40d5-b69d-ff1cf8e82567)

                                      Fig 1.1  Wall Following and Obstacle avoidance


![Screenshot from 2023-04-30 22-36-25](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/c77ad981-579f-4081-8c3e-2028049b3e91)
                                         
                                                    Fig 1.2  Map in Rviz  


![proj_image](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/6a17d736-8ff0-4ae2-aaf9-170d60bec624)
                               
                                 Fig 1.3 Slam algorithm and waypoint Follower in Gazebo and Rviz 
                               

![gazebo environment](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/a3e29448-23ee-4577-830d-786e5ffd2c0b)

               Fig 1.4 Gazebo virtual environment



**Video**

                                   This video shows the Demonstation of the project


[![Watch the video](https://github.com/shivasamkumar/PythonFinalProject/assets/83110296/65ce038a-d478-40d5-b69d-ff1cf8e82567)](https://drive.google.com/file/d/1Q738d2BUip9NrR6repttMF5zozfa0XHT/view?usp=sharing)



## Future versions 
* **Implementing IMU sensors and Control algorithm**

  Integrating IMU sensors and control algorithm for the coustom robot and also implement sensor fusion algorithms

* **Hardware Integration**
