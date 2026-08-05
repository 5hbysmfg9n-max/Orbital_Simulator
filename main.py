from Body import Body
from Simulation import Simulation
from Vector2D import Vector2D
from Visualization import Visualization

# Create the Earth, Moon, and Sun bodies
earth = Body(
    name="Earth",
    mass=5.972e24,
    radius=6.371e6,
    position=Vector2D(1.496e11, 0),
    velocity=Vector2D(0, 2.978e4),
)

moon = Body(
    name="Moon",
    mass=7.348e22,
    radius=1.737e6,
    position=Vector2D(1.496e11 + 3.844e8, 0),
    velocity=Vector2D(0, 2.978e4 + 1.022e3),
)

sun = Body(
    name="Sun",
    mass=1.989e30,
    radius=6.9634e8,
    position=Vector2D(0, 0),
    velocity=Vector2D(0, 0),
)

simulation = Simulation([earth, moon, sun])

dt = 60  # Seconds per simulation step
# Days * hours * minutes * seconds
sim_time = 365 * 24 * 60 * 60 * 10
steps = sim_time // dt

for _ in range(steps):
    simulation.update(dt)

visualization = Visualization(simulation)
visualization.plot_trajectory()
