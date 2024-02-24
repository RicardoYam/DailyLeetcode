#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list = []
        for c in strs[0]:
            list.append(c)
        
        res = ""
        for i, c in enumerate(list):
            for string in strs:
                if i == len(string) or string[i] != c:
                    return res
            res += c
        return res
        


# @lc code=end

