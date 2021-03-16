from onedim.function import Function
from onedim.dichotomy_method import dichotomy_method

def main():
    my_fun = Function()
    # my_fun.plot_func()
    dichotomy_method(my_fun)

    return 
