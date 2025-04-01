from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:

        def prefix(nums: List[int]):
            nums.sort()
            prev = 0
            res = []
            res.append(0)
            for i in range(len(nums)):
                calc = prev + nums[i]
                res.append(calc)
                prev = calc
            return res
        prefixed = prefix(nums)

        i = len(nums)

        while i >= 0:
            arr = nums[i:]
            if sum(arr) > prefixed[i]:
                arr.sort(reverse=True)
                return arr
            i -= 1
        return
