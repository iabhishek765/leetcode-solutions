"""
LC#36 - Valid Sudoku [Medium]
Topic: Hash Set / Array
ML Connection: Constraint checking via hash sets is the same pattern 
used in feature validation pipelines — detecting duplicate or 
conflicting entries before feeding data into a model.
"""

class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_idx = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)

        return True
