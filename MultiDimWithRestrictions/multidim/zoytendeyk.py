import copy 

from typing import List
from multidim.function import Function
from scipy.optimize import linprog

def zoytendeyk(x0: List[float], eta: int, fi0: Function, fi: List[Function]) -> List[float]:
    # Начальный этап
    ksi: List[int] = [1 for idx in range(len(fi) + 1)]
    alpha = 1
    lam = 0.5
    delta = -eta
    x = x0

    #  Поиск начального приближения
    # min_eta = linprog(fi, method='simplex').x[0]
    
    # Основной этап
    while True:
        c = copy.deepcopy(ksi)
        A_ub = [[fun._F1, fun._F2] for fun in zip([fi0], fi)]
        b_ub = [eta * ksi_k for ksi_k in ksi]
        s, eta = linprog(c=c, A_ub=A_ub, b_ub=b_ub, method='simplex').x

        if eta < delta:
            x = [x_k + alpha * s for x_k in x]
        else:
            delta *= lam

        if delta < min([fun.f(x[0], x[1]) for fun in zip([fi0], fi)]) and eta == 0:
            break
    
    return x