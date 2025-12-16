# Edge-Based Drone-to-Drone Detection and Tracking System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Platform](https://img.shields.io/badge/Platform-NVIDIA_Jetson-green)
![ROS2](https://img.shields.io/badge/ROS2-Humble-red)

## Abstract
With the growing integration of unmanned aerial vehicles (UAVs) across commercial, defense, and surveillance domains, the need for autonomous aerial monitoring systems has become increasingly critical.

This project proposes the design and development of a real-time drone-to-drone detection and tracking framework, enabling one UAV to intelligently detect, identify, and follow other drones within its visual field. The system utilizes an onboard camera module for continuous video capture, while all computation is performed locally on an edge platform (NVIDIA Jetson) to achieve real-time processing without cloud connectivity.


## Hardware Requirements
* **Edge Computer:** NVIDIA Jetson (Orin) 
* **Camera Module:** ZED3
* **Flight Controller:** PX4 Autopilot compatible hardware 

## Software Dependencies
* **OS:** Ubuntu 20.04 or 22.04
* **Middleware:** ROS2 Humble, MAVROS2 
* **Deep Learning:** PyTorch (Jetson Build), TorchVision, YOLOv9

