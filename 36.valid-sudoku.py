#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r // 3, c // 3]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                # let 3x3 square as 9 parts in whole board, the first 3x3 would be (0,0)...
                squares[r // 3, c // 3].add(board[r][c])
        return True
# @lc code=end

