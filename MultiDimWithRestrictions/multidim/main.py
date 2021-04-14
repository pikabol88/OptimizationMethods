from multidim.restrictions import plot_restrictions
from multidim.zoytendeyk import zoytendeyk

def main():
    plot_restrictions(point_on_boarder=False)
    plot_restrictions(point_on_boarder=True)

    res = zoytendeyk([0, 0], 1, )
    return