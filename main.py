from typing import List

# alice - x + y = bob - y + x

# 4 - x + y = 2 - y + x
# 2y = 2x - 2
# y = x - 1


# 2 - x + y = 4


# you can use sets for searching
# so you dont have to sort first

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        bobSets = set(bobSizes)

        for i in aliceSizes:
            y = i + (sum(bobSizes) - sum(aliceSizes)) // 2
            if y in bobSets:
                return [i, y]
        return []
