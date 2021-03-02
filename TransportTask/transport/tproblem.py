import tabulate


class TransportProblem:
    def __init__(self, filename):
        self._demand = list()
        self._supply = list()
        self._costs = list()
        self._matrix = list()

        with open(filename, 'r') as f:
            problem = f.read().splitlines()

        supply = problem.pop(0).split()
        self._supply = [int(item) for item in supply]

        demand = problem.pop(0).split()
        self._demand = [int(item) for item in demand]
        
        while len(problem) > 0:
            matrix = problem.pop(0).split(' ')
            self._matrix.append([int(item) for item in matrix])
        
        print("Проверим задачу на замкнутость:")
        
        sum_sup = sum(self._supply)
        sum_dem = sum(self._demand)
        print("Сумма запасов:" + str(sum_sup))
        print("Сумма спросов:" + str(sum_dem))

        if sum_sup > sum_dem:
            print("Приведем задачу к замкнутому виду, добавив фиктовного поставщика")
            self._demand.append(sum_sup - sum_dem)
            for line in self._matrix:
                line.append(0)
        
        elif sum_sup < sum_dem:
            print("Приведем задачу к замкнутому виду, добавив фиктовного заказчика")
            self._supply.append(sum_dem-sum_sup)
            self._matrix.append([0] * len(self._matrix[0]))
            pass
        
        else:    
            print("Задача замкнутого вида")


    def print_table(self):
        rows = list()
        headers = [""]
        for col, item in enumerate(self._demand):
            headers.append(f"consumer {col + 1} needs {item}")
        for row_num, item in enumerate(self._supply):
            cur_row = list()
            cur_row.append(f"supplier {row_num + 1} supplies {item}")
            for col_num in range(len(self._demand)):
                cur_row.append(self._matrix[row_num][col_num])
            rows.append(cur_row)
        # tablefmt="latex"
        print(tabulate.tabulate(rows, headers))


class Shipment:
    def __init__(self, cpu, q, r, c):
        self.quantity = q
        self.cosPerUnit = cpu
        self.c = c
        self.r = r