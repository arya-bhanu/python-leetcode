from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def subsetsOR(a: List[int]):
            x = 0
            for i in a:
                x = x | i
            return x
        max = subsetsOR(nums)
        counter = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print
        return counter
