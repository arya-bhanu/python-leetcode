from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i_nums1 = 0
        i_nums2 = 0
        set_nums_1 = set(nums1)
        set_nums_2 = set(nums2)
        for num in nums1:
            if num in set_nums_2:
                i_nums1 += 1
        for num in nums2:
            if num in set_nums_1:
                i_nums2 += 1
        return [i_nums1, i_nums2]
