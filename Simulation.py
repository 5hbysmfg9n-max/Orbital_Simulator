from Body import Body
from Vector2D import Vector2D

# Simulate gravity and physics engine
class Simulation:
    def __init__(self, bodies, G=6.67430e-11):
        self.bodies = bodies
        self.G = G
        self.time = 0.0
        self.history = {}
        self.time_history = []
        for body in self.bodies:
            self.history[body] = []
        self.record_state()

    def compute_grav_force(self, body1, body2):
        displacement = body2.position - body1.position
        distance = displacement.magnitude()
        if distance == 0:
            return Vector2D(0,0)
        direction = displacement / distance
        force_magnitude = self.G * body1.mass * body2.mass / (distance ** 2)
        force_vector = direction * force_magnitude
        return force_vector

    def compute_net_force(self, body):
        net_force = Vector2D(0, 0)
        for other in self.bodies:
            if other is body:
                continue
            net_force += self.compute_grav_force(body, other)
        return net_force

    # Update simulation
    def update(self, dt):
        forces = {}
        for body in self.bodies:
            forces[body] = self.compute_net_force(body)
        for body in self.bodies:
            acceleration = forces[body] / body.mass
            body.velocity += acceleration * dt
            body.position += body.velocity * dt
        self.time += dt
        self.record_state()
        
    # Recording state of simulation
    def record_state(self):
        self.time_history.append(self.time)
        for body in self.bodies:
            position_copy = Vector2D(body.position.x, body.position.y)
            self.history[body].append(position_copy)


