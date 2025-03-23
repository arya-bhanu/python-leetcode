from typing import List

# naive using sets


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        sets1 = set(nums1)
        sets2 = set(nums2)
        for i in sets1:
            if i in sets2:
                res.append(i)
        return res
