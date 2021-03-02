import numpy as np
import tabulate


class TransportProblem:
    _demand = []
    _supply = []
    _costs = []
    _matrix = []

    def __init__(self, filename):
        with open(filename, 'r') as f:
            problem = f.read().splitlines()
        supply = problem.pop(0).split(' ')
        demand = problem.pop(0).split(' ')
        self._supply = [int(item) for item in supply]
        self._demand = [int(item) for item in demand]
        while len(problem) > 0:
            matrix = problem.pop(0).split(' ')
            self._matrix.append(matrix)
        print("Проверим задачу на замкнутость:")
        sum_sup = sum(self._supply)
        sum_dem = sum(self._demand)
        print("Сумма запасов:" + str(sum_sup))
        print("Сумма спросов:" + str(sum_dem))
        if sum_sup > sum_dem:
            print("Приведем задачу к замкнутому виду, добавив фиктовного поставщика")
            self._demand.append(sum_sup-sum_dem)
            for i in range(len(self._supply)):
                self._matrix[i].append(0)
        elif sum_sup < sum_dem:
            print("Приведем задачу к замкнутому виду, добавив фиктовного заказчика")
            self._supply.append(sum_dem-sum_sup)
            tmp = []
            for i in range(len(self._demand)):
                tmp.append(0)
            self._matrix.append(tmp)
        else:
            print("Задача замкнутого вида")


    def print_table(self):
        res_i = []
        rows = []
        headers = [""]
        num = 0
        for item in self._demand:
            string = "consumer " + str(num) + " need " + str(item)
            headers.append(string)
            num += 1
        num = 0
        for item in self._supply:
            string = "supplier " + str(num) + " supply " + str(item)
            res_i.append(string)
            for j in range(len(self._demand)):
                res_i.append(self._matrix[num][j])
            num += 1
            rows.append(res_i.copy())
            res_i.clear()
        # tablefmt="latex"
        print(tabulate.tabulate(rows, headers))


class Shipment:
    cosPerUnit = 0
    r = 0
    c = 0
    quantity = 0

    def __init__(self, cpu, q, r, c):
        self.quantity = q
        self.cosPerUnit = cpu
        self.c = c
        self.r = r


if __name__ == '__main__':
    print("\nTRANSPORT PROBLEM:\n")
    tp = TransportProblem("problem.txt")
    tp.print_table()
