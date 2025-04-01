import bisect
from typing import List


# naive approach

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        def bin_search(arr: List[int], target: int) -> bool:
            arr.sort()
            index = bisect.bisect_left(arr, target)
            if index != len(arr) and arr[index] == target:
                return True
            return False
        nums.sort()
        i = len(nums) - 1
        while nums[i] > 0 and i >= 0:
            if bin_search(nums, -1 * nums[i]):
                return nums[i]
            i -= 1
        return -1
