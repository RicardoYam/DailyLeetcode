#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def backtracking(x, y, i):
            if i == len(word):
                return True

            if (x < 0 or y < 0 or x >= ROWS or y >= COLS or 
                (x, y) in seen or
                word[i] != board[x][y]):
                return False
             
            seen.add((x, y))
            # true OR false == true
            res = (backtracking(x + 1, y, i + 1) or
                   backtracking(x - 1, y, i + 1) or
                   backtracking(x, y + 1, i + 1) or
                   backtracking(x, y - 1, i + 1))
            seen.remove((x, y))
            return res

        for x in range(ROWS):
            for y in range(COLS):
                if backtracking(x, y, 0):
                    return True
        return False
# @lc code=end

