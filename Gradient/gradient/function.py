import numpy
import pylab
import math


class Function:
    def __init__(self) -> None:
        self.func_str = "$4x_1+x_2+4\sqrt{1+3x_1^2+x_2^2}$"

    def eval(x1: float, x2: float) -> float:
        return 4 * x1 + x2 + 4 * math.sqrt(1 + 3 * x1 * x1 + x2 * x2)

    def plot_lines(self):
        x = numpy.arange(-10, 10, 0.05)
        y = numpy.arange(-10, 10, 0.05)
        xgrid, ygrid = numpy.meshgrid(x, y)

        zgrid = 4 * xgrid + ygrid + 4 * numpy.sqrt(1 + 3 * xgrid ** 2 + ygrid ** 2)

        cs = pylab.contour(xgrid, ygrid, zgrid, 15)
        pylab.clabel(cs, colors="black")
        pylab.xlabel("x1")
        pylab.ylabel("x2")
        pylab.title("Линии уровня функции" + self.func_str)
        pylab.show()
