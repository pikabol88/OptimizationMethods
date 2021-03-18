from transport.tproblem import TransportProblem
from transport.extreme_point import brute_force

import numpy as np


def main():
    print("\nTRANSPORT PROBLEM:\n")
    tp = TransportProblem("problem.txt")
    tp.print_table()

    matrix, free_vec, target = tp.to_canonical()
    brute_solution = brute_force(matrix, free_vec, target)
    brute_solution = np.reshape(brute_solution, (4, 5))
    brute_cost = tp.cost_summary(brute_solution)
    print("\nBrute force solution:")
    print(brute_solution)
    print(f"Total cost is {brute_cost}")

    #tp.northWestCornerRule()
    #tp.steppingStone()
    #tp.print_result()
