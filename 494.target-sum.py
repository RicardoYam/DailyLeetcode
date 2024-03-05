#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # caching repeat values, will make function faster
        dp = {}

        def backtracking(index, total):
            # end if index == len(list)
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]
            
            dp[(index, total)] = (backtracking(index + 1, total + nums[index]) + 
                   backtracking(index + 1, total - nums[index]))
            return dp[(index, total)]

        return backtracking(0, 0)
        
# @lc code=end

