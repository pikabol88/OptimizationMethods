from gradient.function import Function

class Fibonacci:
    def seq(self, n: int) -> int:
        if n in (1, 2):
            return 1
        return self.seq(n - 1) + self.seq(n - 2)

    def method(self, func: Function, a_k, b_k, l, alpha, eps):
        n = 1
        while self.seq(n) <= (b_k - a_k) / l:
            n += 1
        
        lambda_k = list()
        mu_k = list()
        for k in range(1, n - 1):
            lambda_k.append(a_k + self.seq(n - k - 1) / self.seq(n - k + 1) * (b_k - a_k))
            mu_k.append(a_k + self.seq(n - k) / self.seq(n - k + 1) * (b_k - a_k))
        
        while k < n - 2:
            if func.eval(lambda_k) > func.eval(mu_k):
                a_next = lambda_k
                b_next = b_k
                lambda_next = mu_k
                mu_next = a_next + self.seq(n - k - 1) / self.seq(n - k) * (b_next  - a_next)
            else:
                a_next = a_k
                b_next = mu_k
                mu_next = lambda_k
                lambda_next = a_next + self.seq(n - k - 2) / self.seq(n - k) * (b_next  - a_next)
