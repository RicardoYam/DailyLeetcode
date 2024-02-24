#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and ((s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X")) 
            or (s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C")) 
            or (s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"))):
                res += dic.get(s[i + 1]) - dic.get(s[i])
                i += 2
            else:
                res += dic.get(s[i])
                i += 1
        return res

# @lc code=end

