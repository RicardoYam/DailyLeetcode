#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only hold at most one
        # buy and sell in the same day
        # return maximum profit

        # draw a linear graph to mock the whole process
        # BUY LOW, SELL HIGH: compare with the previous day

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        
# @lc code=end

