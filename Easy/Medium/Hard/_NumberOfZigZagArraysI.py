"""
LC#3699 - Number of ZigZag Arrays I [Hard]
Topic: Dynamic Programming / Prefix Sums
ML Connection: Alternating-state DP (inc/dec tracking) mirrors 
state-transition modeling used in sequence models like HMMs.
"""


class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        size = 2 * m  # first m = inc, last m = dec

        
        M = [[0] * size for _ in range(size)]
        for v in range(m):
            for u in range(v):
                M[v][m + u] = 1
            for u in range(v + 1, m):
                M[m + v][u] = 1

        def mat_mult(A, B):
            n_ = len(A)
            res = [[0] * n_ for _ in range(n_)]
            for i in range(n_):
                Ai = A[i]
                for k in range(n_):
                    if Ai[k]:
                        a = Ai[k]
                        Bk = B[k]
                        ri = res[i]
                        for j in range(n_):
                            ri[j] = (ri[j] + a * Bk[j]) % MOD
            return res

        def mat_pow(M, p):
            n_ = len(M)
            result = [[1 if i == j else 0 for j in range(n_)] for i in range(n_)]
            base = M
            while p > 0:
                if p & 1:
                    result = mat_mult(result, base)
                base = mat_mult(base, base)
                p >>= 1
            return result

        vec = [v for v in range(m)] + [m - 1 - v for v in range(m)]

        Mp = mat_pow(M, n - 2)

        final = [0] * size
        for i in range(size):
            s = 0
            for j in range(size):
                if Mp[i][j]:
                    s += Mp[i][j] * vec[j]
            final[i] = s % MOD

        return sum(final) % MOD
