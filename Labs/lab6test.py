import matplotlib.pyplot as plt
import numpy as np

class DataGenerator:
    def __init__(self, num_points=100):
        self.num_points = num_points
        self._random_generator = self._generator_1

    def _generator_1(self, x):
        return np.random.rand()

    def _generator_2(self, x):
        return np.sin(x)

    def _generator_3(self, x):
        return np.sin(5 * x)

    def _generator_4(self, x):
        return np.sin(x) + 0.5 * np.random.rand()

    @property
    def data(self):
        x_values = np.linspace(0, 10, self.num_points)
        y_values = np.array([self._random_generator(x) for x in x_values])
        return x_values, y_values

    def plot_data(self):
        x, y = self.data
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Generated Data')
        plt.show()

if __name__ == "__main__":
    data_generator = DataGenerator(num_points=100)
    
    # Use generator_4() for peaks and valleys
    data_generator._random_generator = data_generator._generator_4
    data_generator.plot_data()

    # Use generator_3() to change the length (or frequency) of the peaks
    data_generator._random_generator = data_generator._generator_3
    data_generator.plot_data()

    # Use generator_2() to get the squiggles
    data_generator._random_generator = data_generator._generator_2
    data_generator.plot_data()
