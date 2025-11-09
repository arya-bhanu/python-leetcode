from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # greedy
        sets = set()
        for car in nums:
            for num in range(car[0], car[1] + 1):
                sets.add(num)
        return len(sets)
