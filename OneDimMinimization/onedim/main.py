from onedim.function import Function
from onedim.dichotomy_method import dichotomy_method
from onedim.parabolic import parabolic
from onedim.parabolic import payell_method
from onedim.dichotomy_method import theoretical_assessment

def main():
    eps_list = [0.1, 0.01, 0.001]
    my_fun = Function()
    print("Function: " + my_fun.func_str + '\n')
    for eps in eps_list:
        print("eps = ", eps)
        print("Dichotomy method results:")
        x, f_x, iterations = dichotomy_method(my_fun, eps)
        print("x = ", x)
        print("f(x) = ", f_x)
        print("Number of function call:")
        print("\t theoretical  = " + str(theoretical_assessment(my_fun, eps)))
        print("\t practical = " + str(iterations))
        print("\n")

    # my_fun.plot_func()
    # print(payel_method(my_fun, 0.001))
    # print(parabolic(my_fun, 0))

    return
