# 🚗 AI-Based Autonomous Navigation System

## 📌 Project Overview

This project simulates an AI-based autonomous navigation system in a 2D grid environment, where a robot intelligently navigates from a user-defined start point to a destination while avoiding obstacles.

The system leverages the A* (A-Star) path planning algorithm to compute the shortest optimal path and dynamically adapts to generated environments.

This project reflects real-world applications such as:
- Self-driving vehicles  
- Warehouse automation  
- Robotics navigation systems  
- Delivery route optimization  

---

## 🎯 Objective

- Enable autonomous navigation in a virtual environment  
- Compute optimal path using heuristic-based search (A*)  
- Avoid obstacles efficiently  
- Provide an interactive simulation for real-time visualization  

---

## 🧠 Technologies Used

- Python – Core programming  
- Pygame – 2D visualization and simulation  
- A* Algorithm – Path planning and optimization  

---

## 🏗️ System Architecture

The system follows a modular architecture:

1. Environment Setup  
   - Grid-based map generation (20x20)  

2. User Input Module  
   - Start and End node selection  

3. Obstacle Handling  
   - Manual placement  
   - Automatic obstacle generation (validated)  

4. Path Planning Engine  
   - A* algorithm computes shortest path  

5. Execution Engine  
   - Robot follows computed path step-by-step  

---

## ⚡ Key Features

- User-defined Start and End points  
- Manual obstacle creation and removal  
- Automatic obstacle generation (press G)  
- Guaranteed valid path before simulation  
- Real-time path visualization  
- Step-by-step robot movement  
- Interactive controls for simulation  

---

## 📂 Project Structure
AI-Based-Autonomous-Navigation-System/
│
├── src/
│ ├── main.py # Main simulation & control logic
│ ├── simulation.py # Rendering & visualization
│ └── path_planning.py # A* algorithm implementation
│
├── images/ # Output screenshots
├── demo/ # Demo video
├── README.md
└── requirements.txt


---

## ⚙️ Installation


pip install pygame

---

## ▶️ How to Run
python src/main.py


---

## 🎮 Controls

| Action               | Key / Input   |
|---------------------|--------------|
| Set Start Point     | S + Click     |
| Set End Point       | E + Click     |
| Generate Obstacles  | G             |
| Add Obstacle        | Left Click    |
| Remove Obstacle     | Right Click   |
| Start Simulation    | SPACE         |
| Reset Grid          | R             |

---

## 🔄 Working Flow

1. User selects Start (S) and End (E) points  
2. Press G to generate obstacles automatically  
3. System ensures a valid path exists using A*  
4. Press SPACE to compute path and move robot  

---

## 🧮 Algorithm Used: A* (A-Star)

f(n) = g(n) + h(n)

Where:
- g(n) = cost from start to current node  
- h(n) = heuristic (Manhattan distance)  
- f(n) = total estimated cost  

- Guarantees shortest path  
- Efficient and widely used in robotics and AI  

---

## 📸 Output Screenshots

![Grid](images/grid.png)  
![Obstacles](images/obstacles.png)  
![Path](images/path1.png)  
![Start-End](images/start_end.png)  

---

## 🎥 Demo Video

Click below to watch the project demo:

👉 [Watch Demo](./demo/demo.mp4)

---

## 🚀 Future Enhancements

- Dynamic obstacle movement with real-time replanning  
- Integration with OpenCV for object detection  
- Implementation of YOLO for obstacle recognition  
- Upgrade to CARLA Simulator for realistic environments  
- Reinforcement Learning-based navigation  

---

## 💡 Learning Outcomes

- Strong understanding of A* path planning algorithm  
- Hands-on experience with simulation-based robotics systems  
- Knowledge of real-time decision making in AI systems  
- Practical exposure to autonomous navigation concepts  

---

## 👩‍💻 Author


Swetha K

