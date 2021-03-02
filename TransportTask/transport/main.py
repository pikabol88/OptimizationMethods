from transport.tproblem import TransportProblem


def main():
    print("\nTRANSPORT PROBLEM:\n")
    tp = TransportProblem("problem.txt")
    tp.print_table()
