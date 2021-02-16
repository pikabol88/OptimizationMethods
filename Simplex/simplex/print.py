import string


def print_task(matrix: list, line_signs: list, free_vec: list, var_signs: list, target: list, message: string):
    print(message)
    print("Matrix of specified conditions with signs and a column of free members")
    for line in matrix:
        print(line)
    print()
    print(line_signs)
    print(free_vec)
    print("Variable sign constraints")
    print(var_signs)
    print("Target function")
    print(target)
    print("============================================================================")