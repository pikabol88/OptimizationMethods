from pathlib import Path

from simplex.canonical import to_canon
from simplex.dual_task import to_dual_task
from simplex.extreme_point import brute_force
from simplex.print import print_task
from simplex.parse import parse
from simplex.simplex import simplex, initialize_simplex


def main():
    message = "***Direct task***"
    matrix, line_signs, free_vec, var_signs, target = parse(Path("config.txt"))
    print_task(matrix, line_signs, free_vec, var_signs, target, message)

    message = "***Dual task***"
    dual_matrix, dual_line_signs, dual_free_vec, dual_var_signs, dual_target = to_dual_task(
        matrix, line_signs, free_vec, var_signs, target)
    print_task(dual_matrix, dual_line_signs, dual_free_vec, dual_var_signs, dual_target, message)

    message = "***Canonical direct task***"
    N, B, A, b, c, v = to_canon(matrix, line_signs, free_vec, var_signs, target)
    print_task(matrix, line_signs, free_vec, var_signs, target, message)

    message = "***Canonical dual task***"
    dual_N, dual_B, dual_A, dual_b, dual_c, dual_v = to_canon(dual_matrix, dual_line_signs, dual_free_vec,
                                                              dual_var_signs, dual_target)
    print_task(dual_matrix, dual_line_signs, dual_free_vec, dual_var_signs, dual_target, message)

    print("***Solution of direct task by brute force method***")
    print(brute_force(A, b, c))
    print()
    print("***Solution of dual task by brute force method***")
    print(brute_force(dual_A, dual_b, dual_c))
    print("============================================================================")

    print("***Solution of direct task by simplex method***")
    N, B, A, b, c, v = initialize_simplex(matrix, free_vec, target)
    print(simplex(N, B, A, b, c, v))

    """
    print()
    print("***Solution of dual task by simplex method***")
    N, B, A, b, c, v = initialize_simplex(dual_matrix, dual_free_vec, dual_target)
    print(simplex(N, B, A, b, c, v))
    print("============================================================================")
    """
