from typing import List


# naive approach

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        def search(nums: List[int], target: int) -> bool:
            i = 0
            j = len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] == target:
                    return True
                elif nums[m] < target:
                    i = m + 1
                else:
                    j = m - 1
            return False
        nums.sort()
        i = len(nums) - 1
        while nums[i] > 0 and i >= 0:
            if search(nums, -1 * nums[i]):
                return nums[i]
            i -= 1
        return -1
