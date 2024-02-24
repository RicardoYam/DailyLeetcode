#
# @lc app=leetcode id=1625 lang=python3
#
# [1625] Lexicographically Smallest String After Applying Operations
#

# @lc code=start
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def addToString(s, a):
            strings = list(s)
            for i in range(len(s)):
                if i % 2 != 0:
                    strings[i] = str((int(s[i]) + a) % 10)
            return ''.join(strings)

        def rotateToString(s, b):
            strings = collections.deque(s)
            for _ in range(b):
                temp = strings.pop()
                strings.appendleft(temp)
            return ''.join(strings)
        
        visited = set()
        def dfs(s):
            if s in visited:
                return
            visited.add(s)
            dfs(addToString(s, a))
            dfs(rotateToString(s, b))
        
        dfs(s)
        return min(visited)

# @lc code=end

