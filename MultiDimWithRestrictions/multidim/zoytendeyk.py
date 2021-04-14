from typing import List
from multidim.function import Function
from scipy.optimize import linprog

def zoytendeyk(x0: List[float], eta: int, fi0: Function, fi: List[Function]) -> List[float]:
    # Начальный этап
    ksi: List[int] = [1 for idx in range(len(fi) + 1)]
    lam = 0.5
    delta = -eta
    xk = x0

    #  Поиск начального приближения
    min_eta = linprog(fi).x[0]
    
    # Основной этап
    
