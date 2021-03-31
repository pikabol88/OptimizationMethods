from gradient.function import OneVarFunction
import math
from typing import Tuple


# Return min point and the value of the function in this point
def dichotomy_method(fun: OneVarFunction, a, b, eps: float) -> Tuple[float, float, int]:
    alpha = (b-a)/100
    iter_num = 0
    while abs(b - a) > eps:
        tmp = (a + b) / 2
        if fun.eval(tmp - alpha) < fun.eval(tmp + alpha):
            b = tmp
        else:
            a = tmp
        iter_num += 1
    fun.min = (a + b) / 2
    return (a + b) / 2#, fun.eval((a + b) / 2), iter_num
