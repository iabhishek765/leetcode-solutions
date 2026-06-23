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

        inc = [v for v in range(m)]          # count of values smaller
        dec = [m - 1 - v for v in range(m)]  # count of values larger

        for step in range(3, n + 1):
            pref_dec = [0] * (m + 1)
            for v in range(m):
                pref_dec[v + 1] = (pref_dec[v] + dec[v]) % MOD

            suf_inc = [0] * (m + 1)
            for v in range(m - 1, -1, -1):
                suf_inc[v] = (suf_inc[v + 1] + inc[v]) % MOD

            new_inc = [0] * m
            new_dec = [0] * m
            for v in range(m):
                new_inc[v] = pref_dec[v]        # sum dec[u], u < v
                new_dec[v] = suf_inc[v + 1]      # sum inc[u], u > v

            inc, dec = new_inc, new_dec

        ans = 0
        for v in range(m):
            ans = (ans + inc[v] + dec[v]) % MOD

        return ans
