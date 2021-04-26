import math
from scipy.optimize import linprog


def main():
    with open("output/matrix.txt", "r") as matrix_file:
        matrix = [[-int(num) for num in line.split()] for line in matrix_file]
    
    with open("output/free_vector.txt", "r") as free_vec_file:
        free_vec = [[-int(num) for num in line.split()] for line in free_vec_file]
    
    with open("output/target_func.txt", "r") as target_func_file:
        target_func = [[float(num) for num in line.split()] for line in target_func_file]

    solution = linprog(c=target_func, A_ub=matrix, b_ub=free_vec, method='simplex').x

    not_zero = list()
    sum = 0
    for idx, num in enumerate(solution):
        if num != 0:
            not_zero.append([idx, math.ceil(num)])
            sum += math.ceil(num)
    print(not_zero)
    print(sum)