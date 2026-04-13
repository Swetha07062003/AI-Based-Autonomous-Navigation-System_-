# 🚗 AI-Based Autonomous Navigation System

## 📌 Project Overview

This project simulates an AI-based autonomous navigation system where a robot navigates from a start point to a destination while avoiding obstacles using an intelligent path planning algorithm.

It demonstrates core concepts used in self-driving cars, robotics, warehouse automation, and delivery systems.

---

## 🎯 Objective

* Enable autonomous navigation in a virtual environment
* Avoid obstacles dynamically
* Compute shortest optimal path using A* algorithm

---

## 🧠 Technologies Used

* Python
* Pygame (2D Simulation)
* A* Algorithm (Path Planning)

---

## 🏗️ Project Architecture

1. Grid-based environment creation
2. Start and End node selection
3. Obstacle placement
4. Path planning using A*
5. Robot movement along computed path

---

## 📂 Project Structure

```
AI-Based-Autonomous-Navigation-System/
│
├── src/
│   ├── main.py
│   ├── simulation.py
│   └── path_planning.py
│
├── images/
│   ├── grid.png
│   ├── obstacles.png
│   ├── path1.png
│   ├── path2.png
│   └── start_end.png
│
├── demo/
│   └── demo.mp4
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Install required library:

```bash
pip install pygame
```

---

## ▶️ How to Run

```bash
python src/main.py
```

---

## 🎮 Controls

| Action           | Key / Input       |
| ---------------- | ----------------- |
| Set Start Point  | Press `S` + Click |
| Set End Point    | Press `E` + Click |
| Add Obstacle     | Left Mouse Click  |
| Remove Obstacle  | Right Mouse Click |
| Start Simulation | Press `SPACE`     |
| Reset Grid       | Press `R`         |

---

## 📸 Output Screenshots

### 🔹 Grid Environment

![Grid](images/grid.png)

### 🔹 Obstacle Placement

![Obstacles](images/obstacles.png)

### 🔹 Path Planning Result

![Path](images/path1.png)

### 🔹 Start and End Points

![Start-End](images/start_end.png)

---

## 🎥 Demo Video

👉 [Watch Demo](demo/demo.mp4)

---

## 🚀 Future Improvements

* Real-time object detection using OpenCV
* Integration with YOLO for obstacle recognition
* Upgrade to CARLA simulator for realistic environment
* Dynamic obstacle avoidance
* Reinforcement learning-based navigation

---

## 💡 Learning Outcomes

* Understanding of A* path planning algorithm
* Simulation of autonomous navigation systems
* Practical exposure to robotics concepts

---

## 👩‍💻 Author

**Swetha K**
