import math
import pylab
from matplotlib import mlab
import numpy as np


class Function:
    def __init__(self) -> None:
        self.func_str = "x^6 + 3*x^2 + 6*x - 1"
        self.x_min = -1
        self.x_max = 0
        self.eps = 0.1
        self.count = 0

    def func(self, x: float) -> float:
        self.count += 1
        return pow(x, 6) + 3 * pow(x, 2) + 6 * x - 1

    def plot_func(self):
        x_list = np.linspace(self.x_min, self.x_max, 100)
        y_list = [self.func(x) for x in x_list]
        pylab.plot(x_list, y_list)
        pylab.show()
