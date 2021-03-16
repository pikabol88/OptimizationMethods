from onedim.function import Function


def dichotomy_method(fun: Function) -> float:
    eps = 0.001
    alpha = fun.eps
    a = fun.x_min
    b = fun.x_max
    iter_num = 1
    if fun.func(a) * fun.func(b) > 0:
        print("No root found")
        
    while abs(b - a) > eps:
        tmp = (a + b) / 2
        if fun.func(tmp - alpha) < fun.func(alpha):
            b = tmp
        else:
            a = tmp
        iter_num += 1
    print("iter = " + str(iter_num))
    return (a + b) / 2, fun.func((a+b)/2)
