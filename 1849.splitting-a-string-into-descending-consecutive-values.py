#
# @lc app=leetcode id=1849 lang=python3
#
# [1849] Splitting a String Into Descending Consecutive Values
#

# @lc code=start
class Solution:
    def splitString(self, s: str) -> bool:
        def backtracing(index, prev):
            if index == len(s):
                return True

            for j in range(index, len(s)):
                val = int(s[index: j + 1])
                # check is the number exactly one less than the prev number
                if val + 1 == prev and backtracing(j + 1, val):
                    return True
            return False 

        # traverse each index for the first number, remain one index for next number
        for i in range(len(s) - 1):
            # get the int number of substring, plus one for the exactly same index position
            val = int(s[:i + 1])
            if backtracing(i + 1, val):
                return True
        return False

        
# @lc code=end

