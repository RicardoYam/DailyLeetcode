#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0], bottoms[0]]:
            missingTop, missingButtom = 0, 0
            for i, pair in enumerate(zip(tops, bottoms)):
                top, buttom = pair
                if not (top == target or buttom == target):
                    break
                if  top != target:
                    missingTop += 1
                if buttom != target:
                    missingButtom += 1
                if i == len(tops) - 1:
                    return min(missingTop, missingButtom)
        return -1

# @lc code=end

