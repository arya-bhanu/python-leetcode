from typing import List

# alice - x + y = bob - y + x

# 4 - x + y = 2 - y + x
# 2y = 2x - 2
# y = x - 1


# 2 - x + y = 4


# accepted using binary search

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()

        def bin_search(cand: int, arr: List[int]) -> bool:
            i = 0
            j = len(arr) - 1
            while i <= j:
                m = (i+j) // 2
                if cand == arr[m]:
                    return True
                elif cand < arr[m]:
                    j = m - 1
                else:
                    i = m + 1
            return False

        for i in aliceSizes:
            y = i + ((sum(bobSizes) - sum(aliceSizes)) // 2)
            if y > 0 and bin_search(y, bobSizes):
                return [i, y]

        return []
