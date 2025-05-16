from typing import List
from collections import OrderedDict


class Solution:
    def mergeArrays(self, x1: List[List[int]], x2: List[List[int]]) -> List[List[int]]:
        dict = {}
        res = []
        if len(x1) < len(x2):
            nums2 = x2
            nums1 = x1
        elif len(x2) <= len(x1):
            nums2 = x1
            nums1 = x2
        for i in range(len(nums2)):
            if i < len(nums1):
                dict[nums2[i][0]] = dict.get(nums2[i][0], 0) + nums2[i][1]
                dict[nums1[i][0]] = dict.get(nums1[i][0], 0) + nums1[i][1]
            else:
                dict[nums2[i][0]] = dict.get(nums2[i][0], 0) + nums2[i][1]
        for key, val in OrderedDict(sorted(dict.items())).items():
            res.append([key, val])
        return res
