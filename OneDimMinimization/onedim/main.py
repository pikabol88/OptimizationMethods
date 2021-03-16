from onedim.function import Function
from onedim.dichotomy_method import dichotomy_method


def main():
    my_fun = Function()
    # my_fun.plot_func()
    x, f_x, iterations = dichotomy_method(my_fun, 0.001)
    print("x = ", x)
    print("f(x) = ", f_x)
    print("iterations =", iterations)
