#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        q = deque([n])
        seen = set()
        seen.add(n)
        ans = 0

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == 1:
                    return ans
                
                # odd
                if cur % 2:
                    if cur + 1 not in seen:
                        q.append(cur + 1)
                        seen.add(cur + 1)
                    if cur - 1 not in seen:
                        q.append(cur - 1)
                        seen.add(cur - 1)
                # even
                else:
                    if cur // 2 not in seen:
                        q.append(cur // 2)
                        seen.add(cur // 2)
            ans += 1
        return ans

        
# @lc code=end

