from typing import List

# using monolithic stack


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        result = [-1] * len(nums1)
        # stores location of each nums1
        for i in range(len(nums1)):
            dict[nums1[i]] = i

        # monolithic stack algorithm
        stack = []
        for i in nums2:
            # we need to peek first in while loop
            while (len(stack) > 0 and stack[-1] < i):
                val = stack[-1]
                result[dict[val]] = i
                stack.pop()
            if i in dict:
                stack.append(i)

        return result
