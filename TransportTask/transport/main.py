from transport.tproblem import TransportProblem
from transport.extreme_point import brute_force


def main():
    print("\nTRANSPORT PROBLEM:\n")
    tp = TransportProblem("problem.txt")
    tp.print_table()

    matrix, free_vec, target = tp.to_canonical()
    print("\nBrute force solution:")
    print(brute_force(matrix, free_vec, target))