from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        for i in range(len(gain)):
            gain[i] = start + gain[i]
            start = gain[i]
        maximum = max(gain)
        return 0 if maximum < 0 else maximum


sol = Solution()
print(sol.largestAltitude([-5, 1, 5, 0, -7]))
print(sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
