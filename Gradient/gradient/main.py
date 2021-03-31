from gradient.DFP import DFP
from gradient.fibonacci import Fibonacci
import matplotlib.pyplot as plot
from gradient.function import Function

def main():
    my_fun = Function()
    # my_fun.plot_lines()
    # my_fun.plot()
    for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
        print(f"epsilon = {eps}")

        print("Newton:")
        res = my_fun.newton(eps=eps)
        my_fun.set_points(res)
        print('\tsolution: ' + str(res[-1]))
        print('\titers: ' + str(my_fun.iter))
        my_fun.plot_lines()

        print("DFP:")
        solver = DFP()
        solution = solver.get_solution((0, 0), eps)
        print('\tsolution: ' + str(solution))
        print('\titers: ' + str(solver.get_iter_num()))

        print("Fibonacci:")
        left, right = 0, 0
        fib = Fibonacci()
        res = fib.method(my_fun, left, right, eps)
        print(f'\tsolution: {res}')
        #print(f'\titers: {my_fun.iter}')
        my_fun.plot_lines()

    solver.draw_contoures()

    plot.ylabel("y")
    plot.xlabel("x")
    plot.title("Линии уровня функции" + my_fun.func_str)
    plot.show()

    return
