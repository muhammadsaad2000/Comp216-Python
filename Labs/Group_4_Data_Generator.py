import random
import matplotlib.pyplot as plt



class SensorDataGenerator:
    def __init__(self, name="Sensor", baseline=0, amplitude=1, frequency=1, squiggle_intensity=0.1):
        self.name = name
        self.baseline = baseline
        self.amplitude = amplitude
        self.frequency = frequency
        self.squiggle_intensity = squiggle_intensity

    def _generate_normalized_value(self):
        # Generate a normalized value between 0 and 1
        return random.uniform(0, 1)

    def generate_sensor_value(self):
        # Generate a sensor value by transforming the normalized value
        normalized_value = self._generate_normalized_value()

        # Apply transformations based on class properties
        value = (
                self.baseline +
                self.amplitude * normalized_value +
                self.squiggle_intensity * (random.uniform(0, 1) - 0.5) +
                self.amplitude * 0.5 * (1 + (2 * normalized_value - 1) * (1 + self.frequency * normalized_value))
        )

        return value

    def generate_data_points(self, num_points=500):
        # Generate a list of data points for plotting
        data_points = [self.generate_sensor_value() for _ in range(num_points)]
        return data_points

    def plot_data(self, num_points=500):
        # Plot the generated data
        data_points = self.generate_data_points(num_points)
        plt.plot(data_points)
        plt.title(f"{self.name} Data Simulation")
        plt.xlabel("Time")
        plt.ylabel("Sensor Value")
        plt.show()


# Example usage:
sensor = SensorDataGenerator(name="Temperature", baseline=18, amplitude=3, frequency=3, squiggle_intensity=0.5)
sensor.plot_data()
