from Vector2D import Vector2D

class Body:
    def __init__(self, name: str, mass: float, radius: float,
                 position: Vector2D, velocity: Vector2D):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity

    def __str__(self):
        return f"{self.name} | mass={self.mass} | radius={self.radius} | pos={self.position} | vel={self.velocity}"