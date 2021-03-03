from tproblem import TransportProblem


def main():
    print("\nTRANSPORT PROBLEM:\n")
    tp = TransportProblem("problem.txt")
    tp.northWestCornerRule()
    tp.steppingStone()
    tp.print_result()
    tp.print_table()
