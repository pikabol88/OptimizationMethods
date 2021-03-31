import pylab
from typing import List, Tuple
import numpy as np
import math


class Function:
    def __init__(self) -> None:
        self.func_str = "$4x_1+x_2+4\sqrt{1+3x_1^2+x_2^2}$"

    def f(self, x1: float, x2: float) -> float:
        return 4 * x1 + x2 + 4 * np.sqrt(1 + 3 * x1 ** 2 + x2 ** 2)

    def eval(x1: float, x2: float) -> float:
        return 4 * x1 + x2 + 4 * math.sqrt(1 + 3 * x1 * x1 + x2 * x2)

    def plot_lines(self) -> None:
        x = np.arange(-10, 10, 0.05)
        y = np.arange(-10, 10, 0.05)
        xgrid, ygrid = np.meshgrid(x, y)

        zgrid = 4 * xgrid + ygrid + 4 * np.sqrt(1 + 3 * xgrid ** 2 + ygrid ** 2)

        cs = pylab.contour(xgrid, ygrid, zgrid, 15)
        pylab.clabel(cs, colors="black")
        pylab.xlabel("x1")
        pylab.ylabel("x2")
        pylab.title("Линии уровня функции" + self.func_str)
        pylab.show()

    def newton(self, x_start: np.array = np.array([1., 1.])) -> List[np.array]:
        x1 = x_start[0]
        x2 = x_start[1]
        res = [x_start]
        eps = 0.1
        F1 = self._F1(x1, x2)
        F2 = self._F2(x1, x2)
        iter = 1
        while np.sqrt(pow(F2, 2) + pow(F1, 2)) > eps:
            print("\niteration # ", iter)
            iter += 1
            F11, F12, F21, F22 = self._hesse_coef(x1, x2)
            print("Hesse matrix", "\n", F11, F12, "\n", F21, F22)
            detH = self._det(F11, F12, F21, F22)
            print("Det = ", detH)
            F1 = self._F1(x1, x2)
            F2 = self._F2(x1, x2)
            x1 = x1 - 1 / detH * (F22 * F1 - F21 * F2)
            x2 = x2 - 1 / detH * (F11 * F2 - F12 * F1)
            print("\nx1 = ", x1, "\nx2 = ", x2, "\nf(x1,x2) =", self.f(x1, x2))
            res.append(np.array([x1, x2]))

        return res

    def _hesse_coef(self, x1: float, x2: float):
        F11 = -36 * pow(x1, 2) / pow((1 + 3 * pow(x1, 2) + pow(x2, 2)), 1.5) + 12 / np.sqrt(
            1 + 3 * pow(x1, 2) + pow(x2, 2))
        F12 = -12 * x1 * (x2 / pow((1 + 3 * pow(x1, 2) + pow(x2, 2)), 1.5))
        F21 = -12 * x1 * (x2 / pow((1 + 3 * pow(x1, 2) + pow(x2, 2)), 1.5))
        F22 = -4 * pow(x2, 2) / pow((1 + 3 * pow(x1, 2) + pow(x2, 2)), 1.5) + 4 / np.sqrt(1 + 3 * (x1 ** 2) + x2 ** 2)
        return F11, F12, F21, F22

    def _det(self, F11: float, F12: float, F21: float, F22: float) -> float:
        return F11 * F22 - F21 * F12

    def _F1(self, x1: float, x2: float) -> float:
        num = 12 * (x1 / np.sqrt(1 + 3 * x1 ** 2 + x2 ** 2)) + 4
        return num

    def _F2(self, x1: float, x2: float) -> float:
        num = 4 * (x2 / np.sqrt(1 + 3 * x1 ** 2 + x2 ** 2)) + 1
        return num
