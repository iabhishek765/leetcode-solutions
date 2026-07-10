"""
LC#52 - N-Queens II [Hard]
Topic: Backtracking
ML Connection: Counting valid constraint-satisfying configurations is 
used in combinatorial optimization for neural architecture search.
"""

class Solution(object):
    def totalNQueens(self, n):
        self.count = 0
        cols = set()
        diag = set()
        anti_diag = set()

        def backtrack(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or (row-col) in diag or (row+col) in anti_diag:
                    continue
                cols.add(col)
                diag.add(row-col)
                anti_diag.add(row+col)
                backtrack(row + 1)
                cols.remove(col)
                diag.remove(row-col)
                anti_diag.remove(row+col)

        backtrack(0)
        return self.count
