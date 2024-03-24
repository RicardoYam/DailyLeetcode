#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy
        # assume we can find a solution within this condition
        if sum(cost) > sum(gas):
            return -1 

        # if we can successfuly interate through the whole list, then it must be the answer of that start index
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        return start
                
                
# @lc code=end

