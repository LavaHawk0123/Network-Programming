<h2> <a href = "https://github.com/LavaHawk0123/Projects/tree/main/IMU_Plugin_ROS"> Streaming Euler,Quartonian angles, Gyroscope and Magnetometer values</a></h2>
After installing ROS and configuring your work environement from: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
if you don't have a /imu topic already published, open another terminal and run

```
cd src
python3 imu_dummy.py
```

run the following commands in /  :

```
git pull https://github.com/LavaHawk0123/Network-Programming.git
cd catkin_ws/src
catkin_create_pkg IMU_stream
cd IMU_stream/src
mv Network-Programming/UGV_Telemetry_Streamer/client_telemetry.py IMU_stream/src
mv Network-Programming/UGV_Telemetry_Streamer/server_telemetry.py IMU_stream/src
catkin_make
```
Then to run the node:
```
cd IMU_stream
rosrun IMU_plugin_ROS server_imu.py
rosrun IMU_plugin_ROS client_imu.py
```
