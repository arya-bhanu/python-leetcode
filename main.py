from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)
        return self.gcd(maximum, minimum)

    def gcd(self, f, s):
        maximum = max(f, s)
        minimum = min(f, s)
        sisa = maximum % minimum
        while sisa != 0:
            maximum = minimum
            minimum = sisa
            sisa = maximum % minimum
        return minimum


s = Solution()
print(s.findGCD([2, 5, 6, 9, 10]))
