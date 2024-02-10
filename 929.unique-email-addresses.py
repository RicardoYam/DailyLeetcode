#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def removeChar(local):
            local = local.replace('.', '')
            for i, char in enumerate(local):
                if char == '+':
                    return local[:i]
            return local

        seen = dict()
        for email in emails:
            local, domain = email.split('@')
            if not domain in seen:
                seen.setdefault(domain, []).append(removeChar(local))
            else:
                if removeChar(local) in seen[domain]:
                    continue
                else:
                    seen[domain].append(local)

        count = 0
        for key in seen:
            count += len(seen[key])
        return count
# @lc code=end

