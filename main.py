from typing import List


# naive approach like other language such: java, js
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for lists in accounts:
            counter = 0
            for w in lists:
                counter += w
            max = counter if counter > max else max
        return max


sol = Solution()
print(sol.maximumWealth([[1, 5], [7, 3], [3, 5]]))
