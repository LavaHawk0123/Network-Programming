<h2> <a href = "https://github.com/LavaHawk0123/Projects/tree/main/IMU_Plugin_ROS"> Streaming Euler,Quartonian angles, Gyroscope and Magnetometer values</a></h2>
After installing ROS and configuring your work environement from: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment

run the following commands in /  :

```
git pull https://github.com/LavaHawk0123/Projects.git
catkin_create_pkg IMU_stream
cd IMU_stream/src
mv IMU_Plugin_ROS/client_imu.py IMU_stream/src
mv IMU_Plugin_ROS/server_imu.py IMU_stream/src
catkin_make
```
Then to run the node:
```
cd IMU_stream
rosrun IMU_plugin_ROS server_imu.py
rosrun IMU_plugin_ROS client_imu.py
```
