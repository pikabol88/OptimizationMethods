from gradient.function import Function
from gradient.fibonacci import Fibonacci

def main():
    my_fun = Function()
    my_fun.plot_lines()


    left, right = 0, 1
    eps = 0.01
    fib = Fibonacci()
    fib.method(left, right)
    return
