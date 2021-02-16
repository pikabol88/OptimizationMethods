from pathlib import Path

from simplex.canonical import to_canon
from simplex.parse import parse


def main():
    matrix, eq, func = parse(Path("config.txt"))
    for line in matrix:
        print(line)
    print()
    print(eq)
    print(func)

    print("============================================================================")

    to_canon(matrix, eq, func, 5)
    for line in matrix:
        print(line)
    print()
    print(eq)
    print(func)