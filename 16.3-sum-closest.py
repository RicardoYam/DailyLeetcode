#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for index in range(len(nums) - 2):
            l, r = index + 1, len(nums) - 1
            while l < r:
                sum = nums[index] + nums[l] + nums[r]
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum > target:
                    r -= 1
                else:
                    l += 1
        return res
        
# @lc code=end

