#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open paranthesis if open < n
        # only add close paranthesis if close < open
        # function end when open == close == n

        stack = []
        res = []
        def backtracing(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtracing(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                backtracing(openN, closeN + 1)
                stack.pop()

        backtracing(0, 0)
        return res
# @lc code=end

