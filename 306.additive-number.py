#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtracking(first, second, remaining):
            if not remaining:
                return True

            sum_two = str(first + second)
            if not remaining.startswith(sum_two):
                return False
            return backtracking(second, first + second, remaining[len(sum_two):])

        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                first, second = num[:i], num[i:j]

                if (len(first) > 1 and first.startswith('0')) or (len(second) > 1 and second.startswith('0')):
                    continue
                if backtracking(int(first), int(second), num[j:]):
                    return True
        return False
        
# @lc code=end

