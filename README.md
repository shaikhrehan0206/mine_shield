# mine_shield
# Mine Shield

## AI-Based Mine Vehicle Safety System

Mine Shield is an AI-based safety system designed to support the detection of mine vehicles and obstacles in low-visibility conditions.

## System Overview

The system uses multiple sensors and AI-based processing to obtain information about nearby vehicles and obstacles.

### Sensors

- Camera / Vision Sensor
- LiDAR
- Radar
- GPS / GNSS

### Processing

- NVIDIA Jetson
- YOLO-based object detection
- Multi-sensor fusion
- Distance estimation
- Relative-speed estimation
- Time-to-Collision (TTC)
- Risk assessment

### Dashboard

The real-time dashboard displays:

- Camera view
- YOLO detection
- LiDAR distance
- Radar distance and relative speed
- GPS / GNSS information
- Vehicle speed
- TTC
- Risk level
- Sensor status

## System Architecture

Camera → YOLO  
LiDAR → Sensor Fusion  
Radar → Sensor Fusion  
GPS/GNSS → Location Data  

YOLO + LiDAR + Radar → Sensor Fusion → TTC → Risk Assessment → Dashboard

## Project Structure

```text
mine_shield/
├── camera/
├── yolo/
├── lidar/
├── radar/
├── gps/
├── sensor_fusion/
├── ttc/
├── dashboard/
├── database/
├── main.py
├── requirements.txt
└── README.md
