#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) // 4
        sides = [0] * 4

        # if side length not an integer
        if length != sum(matchsticks) / 4:
            return False
        
        # make large number at first place, will speed up the function speed
        # if larger number goes first and not meet the length condition, it will return immediately
        matchsticks.sort(reverse=True)

        def backtracking(i):
            # end function
            if i == len(matchsticks):
                return True
            
            # traverse four sides
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtracking(i + 1):
                        return True
                    # backtracking
                    sides[j] -= matchsticks[i]
            return False
        
        return backtracking(0)

        
# @lc code=end

