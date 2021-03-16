from onedim.function import Function
from onedim.dichotomy_method import dichotomy_method
from onedim.parabolic import parabolic

def main():
    my_fun = Function()
    # my_fun.plot_func()
    dichotomy_method(my_fun)

    print(parabolic(my_fun, 1))

    return 
