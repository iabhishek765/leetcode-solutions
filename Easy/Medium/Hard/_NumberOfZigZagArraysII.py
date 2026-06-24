"""
LC#3700 - Number of ZigZag Arrays II [Hard]
Topic: Dynamic Programming / Prefix Sums / Matrix Exponentiation
ML Connection: Alternating-state DP mirrors state-transition modeling 
in sequence models (HMMs); for large n, matrix exponentiation is the 
same technique used to speed up recurrent computations in some ML 
algorithms (e.g., fast power methods in linear RNNs).
"""

class Solution(object):
    def zigZagArrays(self, n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1

        if n == 1:
            return m % MOD

        inc = [v for v in range(m)]
        dec = [m - 1 - v for v in range(m)]

        for step in range(3, n + 1):
            pref_dec = [0] * (m + 1)
            for v in range(m):
                pref_dec[v + 1] = (pref_dec[v] + dec[v]) % MOD

            suf_inc = [0] * (m + 1)
            for v in range(m - 1, -1, -1):
                suf_inc[v] = (suf_inc[v + 1] + inc[v]) % MOD

            new_inc = [pref_dec[v] for v in range(m)]
            new_dec = [suf_inc[v + 1] for v in range(m)]

            inc, dec = new_inc, new_dec

        return sum(inc[v] + dec[v] for v in range(m)) % MOD
