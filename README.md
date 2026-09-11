# Office FPS — Python & Pygame

A lightweight first-person shooter (FPS) developed in **Python** using the **Pygame** library.

The project focuses on building a small interactive 3D environment from scratch, allowing the player to move around, look freely, and interact with different elements of the environment.

The 3D rendering is implemented using a **ray casting** technique, generating a first-person perspective from a 2D map.

## Images of the game

**ordinator view** <img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/e99819fc-e73d-42db-8695-f0c0c34add77" />
**glasses view** <img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/2534ff30-54fc-4d6e-8de1-f65438937b7a" />
**room with the "door"**<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/47a98914-931a-4769-b2b1-e0f39ea60264" />
**a view of the map**<img width="300" height="350" alt="image" src="https://github.com/user-attachments/assets/fc7ffa9f-2f08-4db9-b49c-af106c953099" />

---

## Overview

**Office FPS** is a small experimental FPS engine designed to explore the fundamentals of 3D rendering, player movement, collision detection, and interactive environments using Python.

Rather than relying on a dedicated 3D engine, the project implements its own basic rendering system based on **ray casting**.

This approach projects a 2D level into a pseudo-3D first-person view by calculating the distance between the player and the objects detected by each ray.

---

## Technologies

* **Python**
* **Pygame**
* **Ray Casting**
* **Trigonometry & Mathematics**
* **2D-to-3D Projection**

---

## Features

* First-person player movement
* Mouse-controlled camera rotation
* Real-time 3D wall rendering
* Mini-map
* Interactive doors
* Interactive computer
* Glasses system
* File-system-style interface
* Collision detection
* Interactive environment elements

---

## How It Works

The game world is represented using a simple **2D grid-based map**.

Each character represents a different type of environment element:

| Character | Element     |
| --------- | ----------- |
| `W`       | Wall        |
| `D`       | Door        |
| `C`       | Computer    |
| `0`       | Empty space |

During each frame, the engine casts multiple rays from the player's position in different directions.

Each ray checks for intersections with the environment and determines the distance to the detected object.

The distance is then used to calculate the height of the corresponding wall slice on the screen, creating the illusion of depth and a 3D environment.

The current implementation uses **120 rays per frame** to generate the 3D view.

---

## Controls

| Key       | Action                 |
| --------- | ---------------------- |
| `Z`       | Move forward           |
| `S`       | Move backward          |
| `Q`       | Move left              |
| `D`       | Move right             |
| **Mouse** | Look around            |
| `E`       | Interact               |
| `L`       | Toggle glasses         |
| `↑ / ↓`   | Navigate files         |
| `Esc`     | Close interface / Quit |

> **Note:** Controls are configured for an AZERTY keyboard layout.

---

## Project Structure

```text
fps-pygame/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `main.py`

Contains the game loop, rendering system, player controls, interactions, collision handling, and game logic.

### `requirements.txt`

Lists the Python dependencies required to run the project.

### `.gitignore`

Contains files and directories that should not be tracked by Git.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/fps-pygame.git
cd fps-pygame
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the game:

```bash
python main.py
```

---

## Requirements

* Python **3.x**
* Pygame

You can install Pygame manually with:

```bash
pip install pygame
```

---

## Gameplay

The player explores an office-like environment from a first-person perspective.

Different elements of the environment can be interacted with, including **doors** and **computers**. The project also includes a glasses mechanic and a file-system-inspired interface to make the environment more interactive.

---

## Rendering

The rendering engine is based on **ray casting**, a technique commonly used by early 3D games.

Instead of rendering a complete 3D scene, the engine:

1. Calculates the direction of each ray.
2. Casts the ray into the 2D map.
3. Detects the first obstacle hit.
4. Calculates the distance between the player and the obstacle.
5. Converts that distance into a wall height.
6. Draws the resulting vertical slice on the screen.

Repeating this process across the screen creates a real-time pseudo-3D first-person perspective.

---

## Possible Improvements

Potential future improvements include:

* Textured walls and floors
* Lighting and shadows
* More detailed environments
* Additional interactive objects
* Enemies and AI
* Weapons and shooting mechanics
* Sound effects and music
* More optimized ray casting
* Multiple levels
* Improved UI and animations

---

## License

This project is intended for educational and experimental purposes.

## Author

AWayToCreate - Feel free to explore the code and experiment with the rendering system.

