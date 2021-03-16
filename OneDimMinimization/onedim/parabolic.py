from typing import List

from onedim.function import Function


def parabolic(fun: Function, x: float) -> float:
    eps = 0.1
    iter = 0
    q = 0
    q_prev = 100000000000

    x1 = fun.x_min
    x3 = fun.x_max

    while abs(q - q_prev) > eps:
        iter += 1
        print(iter)
        q_prev = q

        x1 = x1 + (x3 - x1) * 0.25
        x2 = x1 + (x3 - x1) * 0.5
        x3 = x1 + (x3 - x1) * 0.75

        f1 = fun.func(x1)
        f2 = fun.func(x2)
        f3 = fun.func(x3)

        a0 = f1
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * ((f3 - f1) / (x3 - x1)) * ((f2 - f1) / (x2 - x1))

        q = a0 + a1 * (x - x1) + a2 * (x - x1) * (x - x2)

    return q


class PointValue:
    def __init__(self, x, f_x) -> None:
        self.x = x
        self.y = f_x


def payell_method(fun: Function, eps: float):
    h = 0.1
    x1 = 1
    iter_num = 0
    while 1:
        iter_num += 1
        x2 = x1 + h
        f1 = PointValue(x1, fun.func(x1))
        f2 = PointValue(x2, fun.func(x2))
        if f1.y > f2.y:
            x3 = x1 + 2 * h
        else:
            x3 = x1 - h
        f3 = PointValue(x3, fun.func(x3))
        if f1.y < f2.y:
            if f1.y < f3.y:
                f_min = f1
            else:
                f_min = f3
        elif f2.y < f3.y:
            f_min = f2
        else:
            f_min = f3

        a1 = (f2.y - f1.y) / (f2.x - f1.x)
        a2 = 1 / (f3.x - f2.x) * (((f3.y - f1.y) / (f3.x - f1.x)) - ((f2.y - f1.y) / (f2.x - f1.x)))
        x_res = (f2.x - f1.x) / 2 - a1 / 2 * a2
        if abs(x_res - f_min.x) < eps:
            return x_res, fun.func(x_res), iter_num
        else:
            if fun.func(x_res) < f_min.y:
                x1 = x_res
            else:
                x1 = f_min.x
