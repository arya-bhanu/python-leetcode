from typing import List

# use some kinds of permutation, find the possible iteration
# use bruteforce
# 3 loop of bruteforce


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        i = 0
        counter = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                k = j + 1
                while k < len(nums):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        counter += 1
                    k += 1
                j += 1
            i += 1
        return counter
