# Orbital Simulator

2-dimensional orbital mechanics simulator in Python

Models bodies using Newtonian mechanics

Made to learn Python and understand computational physics and scientific visualization.

## Features

- Simulates gravity between multiple bodies in space
- Newton's Law of Gravitation
- N-body simulation in 2-D
- Object-oriented design
- Stores history for visualization
- Uses Matplotlib for trajectories

## Physics

Models gravity through the lens of Newtonian mechanics.

At every time step, the program calculates the gravitational force between all pairs of bodies, which is then summed to calculate the net force on each body. The force is then used to calculate acceleration, and velocities and positions are updated every time step.

Uses Semi-Implicit Euler integration (computing acceleration, then updating velocity before using this new velocity to update position).

## Project Structure

```text
Orbital_Simulator/
│
├── Body.py
├── Main.py
├── README.md
├── requirements.txt
├── Simulation.py
├── Vector2D.py
└── Visualization.py
```

### File Breakdown

**Vector2D.py**

Builds a 2-D vector class that we use for all vector arithmetic.

**Body.py**

Defines a body with its mass, radius, initial position, and velocity.

**Simulation.py**

Builds the physics engine, calculates gravitational forces, and updates body motion.

**Visualization.py**

Generates trajectory graphs from our recorded simulation.

**Main.py**

Generates the simulation, initializes the bodies, runs the simulation, and displays the results.

## Installation

Clone the repository.

```bash
git clone https://github.com/5hbysmfg9n-max/Orbital_Simulator.git
```

Navigate into the project directory.

```bash
cd Orbital_Simulator
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

## How to Use

Run the simulator using

```bash
python3 Main.py
```

Manually adjust your parameters or bodies within `Main.py`.

## Example Output