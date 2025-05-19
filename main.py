from typing import List


# using two pointer
# also slow?

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        length = len(nums)
        left = 0
        right = length - 1

        for i in range(len(nums)):
            j = length - 1 - i
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1
            if nums[j] > pivot:
                result[right] = nums[j]
                right -= 1
        while left <= right:
            result[left] = pivot
            left += 1
        return result
