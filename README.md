# 🧭 A* Pathfinding Visualizer (Pygame)

An interactive **A* Pathfinding Algorithm Visualizer** built using Python and Pygame.
This project helps you understand how the A* algorithm explores nodes and finds the shortest path in a grid.

---

## 🚀 Features

* 🎯 Set **Start** and **End** nodes
* 🧱 Draw and erase **walls/obstacles**
* ⚡ Real-time visualization of the **A* algorithm**
* 🟡 Open nodes (being explored)
* 🔵 Final shortest path display
* 🧼 Clear grid and restart anytime

---

## 🎮 Controls

| Action         | Key / Mouse   |
| -------------- | ------------- |
| Draw Wall      | Left Click    |
| Erase Wall     | Right Click   |
| Set Start Node | Press `S`     |
| Set End Node   | Press `E`     |
| Run Algorithm  | Press `SPACE` |
| Clear Grid     | Press `C`     |

---

## 🧠 Algorithm Used

### A* (A-Star) Algorithm

A* is a popular pathfinding algorithm that finds the shortest path using:

* **g(n)** → Cost from start to current node
* **h(n)** → Heuristic (Manhattan distance)
* **f(n) = g(n) + h(n)**

It guarantees the shortest path while being efficient.
