from pathlib import Path

from simplex.canonical import to_canon
from simplex.dual_task import to_dual_task
from simplex.print import print_task
from simplex.parse import parse


def main():
    message = "***Direct task***"
    matrix, line_signs, free_vec, var_signs, target = parse(Path("config.txt"))
    print_task(matrix, line_signs, free_vec, var_signs, target, message)

    message = "***Dual task***"
    dual_matrix, dual_line_signs, dual_free_vec, dual_var_signs, dual_target = to_dual_task(
        matrix, line_signs, free_vec, var_signs, target)
    print_task(dual_matrix, dual_line_signs, dual_free_vec, dual_var_signs, dual_target, message)

    message = "***Canonical direct task***"
    to_canon(matrix, line_signs, var_signs, target)
    print_task(matrix, line_signs, free_vec, var_signs, target, message)

    message = "***Canonical dual task***"
    to_canon(dual_matrix, dual_line_signs, dual_var_signs, dual_target)
    print_task(dual_matrix, dual_line_signs, dual_free_vec, dual_var_signs, dual_target, message)
