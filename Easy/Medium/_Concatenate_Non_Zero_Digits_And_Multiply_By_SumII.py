"""
LC#3756 - Concatenate Non-Zero Digits and Multiply by Sum II [Medium]
Topic: Prefix Sum / String
ML Connection: Range query preprocessing via prefix arrays is the same 
technique used in efficient attention mask computation in Transformers.
"""

class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        m = len(s)

        # cnt[i] = number of non-zero digits in s[0..i-1]
        cnt = [0] * (m + 1)
        # prefix_x[i] = x formed by non-zero digits in s[0..i-1] mod MOD
        prefix_x = [0] * (m + 1)
        # prefix_sum[i] = sum of non-zero digits in s[0..i-1]
        prefix_sum = [0] * (m + 1)

        for i in range(m):
            d = int(s[i])
            cnt[i+1] = cnt[i]
            prefix_x[i+1] = prefix_x[i]
            prefix_sum[i+1] = prefix_sum[i]
            if d != 0:
                cnt[i+1] = cnt[i] + 1
                prefix_x[i+1] = (prefix_x[i] * 10 + d) % MOD
                prefix_sum[i+1] = prefix_sum[i] + d

        result = []
        for l, r in queries:
            k = cnt[r+1] - cnt[l]  # count of non-zero digits in [l,r]
            if k == 0:
                result.append(0)
                continue
            # x(l,r) = prefix_x[r+1] - prefix_x[l] * 10^k
            x = (prefix_x[r+1] - prefix_x[l] * pow(10, k, MOD)) % MOD
            digit_sum = prefix_sum[r+1] - prefix_sum[l]
            result.append(x * digit_sum % MOD)

        return result
