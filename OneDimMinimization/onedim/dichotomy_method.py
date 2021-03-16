from onedim.function import Function


def dichotomy_method(fun: Function) -> float:
    eps = 0.001
    alpha = fun.eps
    a = fun.x_min
    b = fun.x_max
    iter_num = 1
    while b - a > eps:
        tmp1 = (a + b) / 2 - alpha
        tmp2 = (a + b) / 2 + alpha
        if fun.func(tmp1) > fun.func(tmp2):
            a = tmp1
        else:
            b = tmp2
        iter_num += 1
    print("iter = " + str(iter_num))
    return (a + b) / 2
