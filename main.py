from typing import List

# solved


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        k = len(nums) - 1
        j = k - 1
        i = k - 2
        while i >= 0:
            if nums[i] + nums[j] > nums[k]:
                return nums[i] + nums[j] + nums[k]

            i -= 1
            j -= 1
            k -= 1
        return 0
