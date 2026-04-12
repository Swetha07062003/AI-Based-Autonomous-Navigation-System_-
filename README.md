# 🚀 AI-Based Autonomous Navigation System

## 📌 Project Overview

This project demonstrates an AI-based autonomous navigation system where a virtual robot navigates from a start point to a destination while avoiding obstacles using intelligent path planning.

---

## 🎯 Objective

To simulate how autonomous robots and self-driving systems make navigation decisions without human intervention.

---

## 🌍 Industry Relevance

Autonomous navigation systems are widely used in:

* Self-driving cars (Tesla, Waymo)
* Warehouse robots (Amazon Robotics)
* Delivery robots
* Drones and UAV systems
* Industrial automation and smart mobility

---

## 🧠 Key Features

* Interactive grid-based simulation
* Start and End point selection
* Real-time obstacle placement and removal
* Automatic obstacle generation (press **G**)
* A* path planning algorithm
* Real-time path re-planning
* Autonomous robot movement
* Screenshot saving feature (press **P**)
* Demo video included

---

## 🛠️ Tech Stack

* Python
* Pygame
* A* Path Planning Algorithm

---

## 🧠 System Architecture

User Input → Grid Creation → Obstacle Detection → Path Planning (A*) → Navigation → Visualization

### Modules:

* `main.py` → Handles user interaction and control logic
* `path_planning.py` → Implements A* algorithm
* `simulation.py` → Handles visualization and rendering

---

## 📂 Folder Structure

AI-Autonomous-Navigation-System/
│
├── demo/
│   └── demo.mp4
├── images/
│   ├── grid.png
│   ├── obstacles.png
│   ├── path1.png
│   ├── path2.png
│   ├── path3.png
│   └── start_end.png
├── main.py
├── simulation.py
├── path_planning.py
├── output.png
├── README.md
├── requirements.txt

---

## ⚙️ Installation

Install dependencies:

pip install pygame

---

## ▶️ How to Run

python main.py

---

## 🎮 Controls

| Action             | Key         |
| ------------------ | ----------- |
| Select Start       | S           |
| Select End         | E           |
| Start Robot        | SPACE       |
| Add Obstacle       | Left Click  |
| Remove Obstacle    | Right Click |
| Reset Grid         | R           |
| Generate Obstacles | G           |
| Save Screenshot    | P           |

---

## 🎥 Demo Video

[Watch Demo](demo/demo.mp4)

---

## 📸 Screenshots

### Grid

![Grid](images/grid.png)

### Start and End

![Start-End](images/start_end.png)

### Obstacles

![Obstacles](images/obstacles.png)

### Path Visualization

![Path1](images/path1.png)
![Path2](images/path2.png)
![Path3](images/path3.png)

---

## 📊 Results

* Robot successfully finds shortest path using A* algorithm
* Avoids obstacles dynamically
* Demonstrates real-time navigation logic
* Re-plans path when environment changes

---

## 🔮 Future Enhancements

* Real-time camera integration using OpenCV
* Object detection using YOLO
* Integration with ROS (Robot Operating System)
* 3D simulation using CARLA simulator
* Reinforcement learning-based navigation
* Multi-agent (multiple robots) system
* Autonomous drone navigation

---

## 🎓 Learning Outcomes

* Understanding of path planning algorithms (A*)
* Hands-on experience with autonomous systems
* Simulation of real-world navigation problems
* Problem-solving using grid-based environments
* Basics of robotics and AI navigation systems

---

## 👩‍💻 Author

Swetha K
