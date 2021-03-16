from typing import List

from onedim.function import Function

def parabolic(fun: Function, x: float) -> float:
    x1 = fun.x_min
    x2 = (fun.x_min + fun.x_max) / 2
    x3 = fun.x_max

    f1 = fun.func(x1)
    f2 = fun.func(x2)
    f3 = fun.func(x3)

    a0 = f1
    a1 = (f2 - f1) / (x2 - x1)
    a2 = (1 / (x3 - x2)) * ((f3 - f1) / (x3 - x1)) * ((f2 - f1) / (x2 - x1))

    q = a0 + a1 * (x - x1) + a2 * (x - x1) * (x - x2)

    return q
