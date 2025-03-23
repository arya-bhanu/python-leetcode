from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        return [True if extraCandies + great >= maxNum else False for great in candies]


sol = Solution()
print(sol.kidsWithCandies([12, 1, 12], 3))
