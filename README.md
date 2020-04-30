# Obstacle-Avoidance-Bot-Using-ROS
This project contains a bot simulation in Gazebo which can avoid obstacles. The robot design and other requirements can be found in this [PDF](assignment.pdf). 
The obstacle avoid is available in both cpp and python languages.
Xacro is used in the project to clean the URDF code.

## Getting Started

1. Clone this repository in the `src` folder of your `catkin` workspace
2. Run `catkin_make`
3. Go to obstacle-avoid.py and make it executable using `chmod +x obstacle_avoidance.py`. No need to do this step if you are using the obstacle-avoid.cpp code.
3. Open 3 Terminals
4. Run the command `roslaunch Obstacle-Avoidance-Bot-Using-ROS spawn.launch`. 
5. In the second terminal run the command `rosrun Obstacle-Avoidance-Bot-Using-ROS obstacle_avoidance.py` or `rosrun Obstacle-Avoidance-Bot-Using-ROS obstacle_avoidance.cpp`
6. In last terminal, run the command `rosrun gazebo_ros gazebo --verbose` to start the robot and begin the obstacle avoidance course.
7. Add blocks in between wherever you want or you can download a world from anywhere else and spawn the bot there.

## Prerequisites

* [ROS](http://wiki.ros.org/kinetic)  
* [Gazebo](http://wiki.ros.org/gazebo_ros_pkgs)


## Video

[![Obstacle-Avoidance-Using-ROS-And-Gazebo](https://youtu.be/4ECO572d5kQ.jpg)](https://youtu.be/4ECO572d5kQ "Obstacle-Avoidance-Using-ROS-And-Gazebo")

## To-Do / Improvements

* Decrease the size/complexity of obstacle_avoidance.cpp code

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Reference
[Construct YouTube Channel](https://www.theconstructsim.com/ros-projects-exploring-ros-using-2-wheeled-robot-part-1/)
