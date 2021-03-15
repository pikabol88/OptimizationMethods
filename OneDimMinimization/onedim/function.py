import math
import pylab
from matplotlib import mlab
import numpy as np


class Function:
    func_str = "x^6 + 3x^2 + 6x - 1"
    x_min = -1
    x_max = 0
    eps = 0.1

    def func(self, x):
        return pow(x, 6) + 3 * pow(x, 2) + 6 * x - 1

    def plot_func(self):
        x_list = np.linspace(self.x_min, self.x_max, 100)
        y_list = [self.func(x) for x in x_list]
        pylab.plot(x_list, y_list)
        pylab.show()
