from gradient.fibonacci import Fibonacci
from gradient.function import Function

def main():
    my_fun = Function()
    my_fun.plot_lines()
    my_fun.newton()

    left, right = 0, 1
    eps = 0.01
    fib = Fibonacci()
    fib.method(left, right)
    return
