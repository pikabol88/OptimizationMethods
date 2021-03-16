from onedim.function import Function


# Return min point and the value of the function in this point
def dichotomy_method(fun: Function, eps: float) -> (float, float, int):
    alpha = fun.eps
    a = fun.x_min
    b = fun.x_max
    iter_num = 0
    if fun.func(a) * fun.func(b) > 0:
        print("No root found")
    while abs(b - a) > eps:
        tmp = (a + b) / 2
        if fun.func(tmp - alpha) < fun.func(alpha):
            b = tmp
        else:
            a = tmp
        iter_num += 1
    return (a + b) / 2, fun.func((a + b) / 2), iter_num