from typing import List

# naive ways using dictionary
# naive using bruteforce


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        result = [-1] * len(nums1)
        for i in range(len(nums1)):
            dict[nums1[i]] = i
        for i in range(len(nums2) - 1):
            if nums2[i] not in dict:
                continue
            for x in range(i + 1, len(nums2)):
                if nums2[x] > nums2[i]:
                    result[dict[nums2[i]]] = nums2[x]
                    break
        return result
