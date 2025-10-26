# 8-Puzzle Search Project

This project implements **Greedy Best-First Search** and **A\* Search** algorithms to solve the classic **8-Puzzle problem** using three different heuristic functions.

---

## 📦 Features
- **Two search algorithms**
  - Greedy Best-First Search  
  - A\* Search
- **Three heuristic functions**
  1. **Number of Misplaced Tiles** – counts tiles not in the correct position.  
  2. **Total Manhattan Distance** – sum of the grid distances from each tile to its goal position.  
  3. **Total Array Index Distance** – sum of the absolute differences between current and goal indices for each tile.  

---

## 🧠 Environment
- **Python** 3.13  
- No external libraries required (only the Python Standard Library).  

---

## 🚀 How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/xingchi-y/8Puzzle
   cd 8Puzzle
   python main.py
