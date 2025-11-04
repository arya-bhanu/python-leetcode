from typing import List


class Solution:
    # greedy solution
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = 0
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if abs(nums[i] - nums[j]) == k:
                    counter += 1
                j += 1
            i += 1
        return counter
