"""
LC#38 - Count and Say [Medium]
Topic: String / Simulation
ML Connection: Run-length encoding is a simple form of data compression — 
similar in spirit to tokenization, where repeated patterns are reduced 
before being fed into a model.
"""

class Solution(object):
    def countAndSay(self, n):
        result = "1"

        for _ in range(n - 1):
            next_result = []
            i = 0
            while i < len(result):
                ch = result[i]
                count = 0
                while i < len(result) and result[i] == ch:
                    count += 1
                    i += 1
                next_result.append(str(count) + ch)
            result = "".join(next_result)

        return result
