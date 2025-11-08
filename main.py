from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        i = 0
        while i < len(nums):
            sum += nums[i]
            i += 2
        return sum
