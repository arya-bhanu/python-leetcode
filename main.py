from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maps = {}
        raws = nums[:]
        nums.sort()
        result = []

        for raw in raws:
            if raw in maps:
                result.append(maps[raw])
                continue
            counter = 0
            j = 0
            while nums[j] < raw and j < len(raws):
                counter += 1
                j += 1
            maps[raw] = counter
            result.append(counter)
        return result
