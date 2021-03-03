from transport.tproblem import TransportProblem
from transport.extreme_point import brute_force

import numpy as np


def main():
    print("\nTRANSPORT PROBLEM:\n")
    tp = TransportProblem("problem.txt")

    matrix, free_vec, target = tp.to_canonical()
    brute_solution = brute_force(matrix, free_vec, target)
    print("\nBrute force solution:")
    print(np.reshape(brute_solution, (4, 5)))

    #tp.northWestCornerRule()
    #tp.steppingStone()
    tp.print_result()
    tp.print_table()

    