from typing import Counter, List

# solved


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        counts = Counter(nums)
        for i in range(len(nums)):
            size = len(nums) - i
            if nums[i] < size:
                continue
            if nums[i] == size:
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                return nums[i]
            if nums[i] > size:
                between = 0 if i == 0 else nums[i-1]
                if size > between and size < nums[i]:
                    if i != 0 and nums[i] == nums[i-1]:
                        continue
                    return size
        return -1
