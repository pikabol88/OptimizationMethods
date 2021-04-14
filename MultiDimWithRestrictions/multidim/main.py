from multidim.restrictions import plot_restrictions
from multidim.zoytendeyk import zoytendeyk

import numpy as np

def main():
    
    # plot_restrictions(point_on_boarder=False)
    # plot_restrictions(point_on_boarder=True)

    res = zoytendeyk([0.2, 0.4], 0.5)
    print(res)
    return