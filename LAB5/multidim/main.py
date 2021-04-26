from multidim.restrictions import plot_restrictions
from multidim.zoytendeyk import zoytendeyk, func, rest

def main():
    
    # plot_restrictions(point_on_boarder=False)
    # plot_restrictions(point_on_boarder=True)

    x0 = [-0.2, -0.4]
    eta0 = -max([fun(x0) for fun in rest])

    res = zoytendeyk(x0, eta0)
    print(f"Answer: {res}")
    print(f"f(x) = {func(res)}")
    
    return