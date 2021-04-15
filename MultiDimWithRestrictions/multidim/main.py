from multidim.restrictions import plot_restrictions
from multidim.zoytendeyk import zoytendeyk, func

def main():
    
    plot_restrictions(point_on_boarder=False)
    plot_restrictions(point_on_boarder=True)

    res = zoytendeyk([-0.2, -0.4], 0.1)
    print(f"Answer: {res}")
    print(f"f(x) = {func(res)}")
    return