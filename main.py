
from typing import List
import copy


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ori = copy.deepcopy(heights)
        heights.sort()
        counter = 0
        i = 0
        for val in ori:
            if val != heights[i]:
                counter += 1
            i += 1
        return counter


sol = Solution()
print(sol.heightChecker([1, 2, 3, 4, 5]))
