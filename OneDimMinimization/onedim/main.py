from onedim.function import Function
from onedim.dichotomy_method import dichotomy_method
from onedim.parabolic import parabolic


def main():
    my_fun = Function()
    # my_fun.plot_func()
    x, f_x, iterations = dichotomy_method(my_fun, 0.001)
    print("x = ", x)
    print("f(x) = ", f_x)
    print("iterations =", iterations)


    print(parabolic(my_fun, 0))

    return 

