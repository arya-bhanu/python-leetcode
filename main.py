from typing import List

# brute force O(mn) time complexity


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        counter = 0
        for i in arr1:
            flag = True
            for j in arr2:
                if abs(j - i) <= d:
                    flag = False
            if (flag):
                counter += 1
        return counter

    # def search(self, nums: List[int], target: int, d: int) -> int:
    #     counter = 0
    #     nums.sort()
    #     i = 0
    #     j = len(nums) - 1
    #     while i <= j:
    #         m = (i + j) // 2
    #         if abs(nums[m] - target) <= d:
    #             counter += 1

    #     return counter
