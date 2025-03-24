from typing import List


# naive approach
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        nums.sort()
        lastIndex = len(nums) - 1
        for i in range(len(nums) // 2):
            averages.append((nums[i] + nums[lastIndex - i]) / 2)
        return min(averages)
