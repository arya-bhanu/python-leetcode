from typing import List

# if it strictly increasing and unique


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        sets = set()
        for num in nums:
            if num - diff in sets and num - diff * 2 in sets:
                counter += 1
            sets.add(num)
        return counter
