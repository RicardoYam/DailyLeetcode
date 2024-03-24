#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def compare(n1, n2):
            # say if we input n1 = 3, n2 = 30
            # then we have 330 > 303
            # in the key function, the first value is later, so we would have a list that had [..., 3, 30, ...] 
            # so we should return -1, swap the order and let it return [..., 30, 3, ...]
            if n1 + n2 > n2 + n1:
                return -1
            # include equal, but we don't care about the order when they equal
            else:
                return 1
        
        nums = sorted(nums, key = cmp_to_key(compare))
        # the reason why we use str(int()) because it may return "000", so we transfer "000" to "0" in this way
        return str(int(''.join(nums)))
        
# @lc code=end

