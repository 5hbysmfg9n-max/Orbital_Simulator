from Body import Body
from Vector2D import Vector2D

earth = Body(
    "Earth",
    5.972e24,
    6.371e6,
    Vector2D(1.496e11, 0),
    Vector2D(0, 29780)
)

print(earth)