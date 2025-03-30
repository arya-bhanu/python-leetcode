from typing import List


# use two pointers
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        nums.sort()
        pos = 0
        neg = 0
        i = 0
        j = len(nums) - 1
        while i <= j:
            if i == j:
                if nums[i] < 0:
                    neg += 1
                elif nums[i] > 0:
                    pos += 1
            else:
                if nums[i] < 0:
                    neg += 1
                elif nums[i] > 0:
                    pos += 1
                if nums[j] < 0:
                    neg += 1
                elif nums[j] > 0:
                    pos += 1
            i += 1
            j -= 1
        return max(pos, neg)
