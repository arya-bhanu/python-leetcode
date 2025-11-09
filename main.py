from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # greedy
        repeated = -1
        missing = -1
        length_grid = len(grid)
        length = length_grid * length_grid
        dicts = {}
        for row in grid:
            for col in row:
                if col not in dicts:
                    dicts[col] = 1
                    continue
                curr = dicts[col]
                curr += 1
                dicts[col] = curr
                repeated = col
        for i in range(1, length + 1):
            if i not in dicts:
                missing = i
        return [repeated, missing]
