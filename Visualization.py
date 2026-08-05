import matplotlib.pyplot as plt


# To visualize the simulation
class Visualization:

    def __init__(self, simulation):
        self.simulation = simulation

    # Graphing trajectories of bodies
    def plot_trajectory(self):
        plt.figure(figsize=(8, 8))
        for body in self.simulation.bodies:
            positions = self.simulation.history[body]
            x_values = []
            y_values = []
            for position in positions:
                x_values.append(position.x)
                y_values.append(position.y)
            plt.plot(x_values, y_values, label=body.name)
            plt.scatter(x_values[-1], y_values[-1], s=50)

        # For graph components
        plt.xlabel("x position (m)")
        plt.ylabel("y position (m)")
        plt.title("Orbital Trajectory")
        plt.axis("equal")
        plt.legend()
        plt.grid()
        plt.show()
