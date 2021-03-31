from gradient.DFP import DFP
from gradient.fibonacci import Fibonacci
import matplotlib.pyplot as plot
from gradient.function import Function

def main():
    my_fun = Function()
    # my_fun.plot_lines()
    # my_fun.plot()
    print("Newton:")
    res = my_fun.newton()
    my_fun.set_points(res)
    print('\tsolution: ' + str(res[-1]))
    print('\titers: ' + str(my_fun.iter))
    my_fun.plot_lines()

    print("DFP:")
    solver = DFP()
    solution = solver.get_solution((0, 0), 0.01)
    print('\tsolution: ' + str(solution))
    print('\titers: ' + str(solver.get_iter_num()))

    solver.draw_contoures()

    plot.ylabel("y")
    plot.xlabel("x")
    plot.title("Линии уровня функции" + my_fun.func_str)
    plot.show()
  
    left, right = 0, 1
    eps = 0.01
    fib = Fibonacci()
    print(fib.method(left, right))
    return
