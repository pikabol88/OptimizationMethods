from pathlib import Path

from simplex.canonical import to_canon
from simplex.parse import parse


def main():
    matrix, line_signs, free_vec, var_signs, target = parse(Path("config.txt"))
    for line in matrix:
        print(line)
    print()
    print(line_signs)
    print(free_vec)
    print(var_signs)
    print(target)

    print("============================================================================")

    #to_canon(matrix, var, func, 5)
    #for line in matrix:
    #    print(line)
    #print()
    #print(eq)
    #print(func)