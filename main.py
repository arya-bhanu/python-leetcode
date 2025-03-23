from typing import List


# one liner
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(x) for x in accounts)


sol = Solution()
print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))
