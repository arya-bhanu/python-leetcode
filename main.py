from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            counted = self.counterSum(start, i, nums)
            sum += counted
        return sum

    def counterSum(self, start: int, end: int, nums):
        sum = 0

        while start <= end:
            sum += nums[start]
            start += 1

        return sum
