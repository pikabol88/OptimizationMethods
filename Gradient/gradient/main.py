from gradient.DFP import DFP
from gradient.fibonacci import Fibonacci
from gradient.function import Function

def main():
    my_fun = Function()
    # my_fun.plot_lines()
    # my_fun.plot()
    print("Newton:")
    res = my_fun.newton()
    print('\tsolution: ' + str(res[-1]))
    print('\titers: ' + str(my_fun.iter))

    print("DFP:")
    solver = DFP()
    solution = solver.get_solution((1, 1), 0.01)
    print('\tsolution: ' + str(solution))
    print('\titers: ' + str(solver.get_iter_num()))

    left, right = 0, 1
    eps = 0.01
    fib = Fibonacci()
    fib.method(left, right)
    return
