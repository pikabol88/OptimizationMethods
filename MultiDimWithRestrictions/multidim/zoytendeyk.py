from typing import List
from scipy.optimize import linprog

import numpy as np


func = lambda x: 4 * x[0] + x[1] + 4 * np.sqrt(1 + 3 * x[0] ** 2 + x[1] ** 2)
func_grad = lambda x: [12 * (x[0] / np.sqrt(1 + 3 * x[0] ** 2 + x[1] ** 2)) + 4,
                       4 * (x[1] / np.sqrt(1 + 3 * x[0] ** 2 + x[1] ** 2)) + 1]

rest = [
    lambda x: -x[0],
    lambda x: x[0] - 2 * x[1] - 0.3,
    lambda x: -x[0] + 2 * x[1] - 1,
    lambda x: x[0] + x[1] - 1
]

rest_grads = [
    lambda x: [-1, 0],
    lambda x: [1, -2],
    lambda x: [-1, 2],
    lambda x: [1, 1]
]


def get_bounds(x, delta):
    res = []
    for idx in range(len(rest)):
        if -delta <= rest[idx](x) <= 0.0:
            res.append(idx)
    return res


def simplex(x_k, d_k):
    bounds_idxs = get_bounds(x_k, d_k)
    aux_matrix = np.zeros(shape=(1 + len(bounds_idxs), 3))

    aux_matrix[:, 2] = -1
    aux_matrix[0, 0:2] = func_grad(x_k)

    j = 1
    for i in bounds_idxs:
        aux_matrix[j, 0:2] = rest_grads[i](x_k)
        j += 1

    target_coefs = np.zeros(3)
    target_coefs[2] = 1

    bias = np.zeros(aux_matrix.shape[0])
    bounds = [[-1, 1], [-1, 1], [None, None]]

    return linprog(c=target_coefs, A_ub=aux_matrix, b_ub=bias, bounds=bounds, method='simplex').x


def zoytendeyk(x0: List[float], eta: int) -> List[float]:
    # Начальный этап
    alpha = 1
    lam = 0.5
    delta = -eta
    x = x0

    # Основной этап
    while True:
        *s, eta = simplex(x, delta)

        if eta < delta:
            x = [x_k + alpha * s_k for x_k, s_k in zip(x, s)]
        else:
            delta *= lam
        
        print(x)

        if delta < min([func(x)] + [r(x) for r in rest]) and eta < 1e-6:
            break
    
    return x