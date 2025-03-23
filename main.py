from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        i = 1
        j = len(mountain) - 1
        while (i < j):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                res.append(i)
            i += 1
        return res
