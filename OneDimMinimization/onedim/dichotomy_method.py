from onedim.function import Function
import math
from typing import Tuple


# Return min point and the value of the function in this point
def dichotomy_method(fun: Function, eps: float) -> Tuple[float, float, int]:
    a = fun.x_min
    b = fun.x_max
    alpha = (b-a)/100
    iter_num = 0
    while abs(b - a) > eps:
        tmp = (a + b) / 2
        if fun.func(tmp - alpha) < fun.func(tmp + alpha):
            b = tmp
        else:
            a = tmp
        iter_num += 1
    return (a + b) / 2, fun.func((a + b) / 2), iter_num


def theoretical_assessment(fun: Function, eps: float) -> int:
    return math.ceil(abs((math.log2((fun.x_max - fun.x_min) / 2 * eps) + 1))) * 2
