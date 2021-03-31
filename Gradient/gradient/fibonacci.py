from gradient.function import Function

class Fibonacci:
    def seq(self, n: int) -> int:
        if n in (1, 2):
            return 1
        return self.seq(n - 1) + self.seq(n - 2)

    def method(self, func: Function, a_k, b_k):
        l = b_k - a_k
        alpha = l / 100

        n = 1
        while self.seq(n) <= (b_k - a_k) / l:
            n += 1
        
        # k = 1
        lambda_k = a_k + self.seq(n - 2) / self.seq(n) * (b_k - a_k)
        mu_k = a_k + self.seq(n - 1) / self.seq(n) * (b_k - a_k)
        
        # k <= n - 2
        for k in range(1, n - 1):
            if func.f(lambda_k) > func.f(mu_k):
                a_k, b_k, lambda_k = lambda_k, b_k, mu_k
                mu_k = a_k + self.seq(n - k - 1) / self.seq(n - k) * (b_k - a_k)
            else:
                a_k, b_k, mu_k = a_k, mu_k, lambda_k
                lambda_k = a_k + self.seq(n - k - 2) / self.seq(n - k) * (b_k  - a_k)
        
        # k = n - 1
        lambda_n = lambda_k
        mu_n = lambda_n + alpha

        if func.f(lambda_n) == func.f(mu_n):
            a_n = lambda_n
            b_n = b_k
        else:
            a_n = a_k
            b_n = mu_n

        return (a_n + b_n) / 2
