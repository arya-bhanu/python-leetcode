from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]):
        pIndex = 0
        while pIndex < len(arr) - 1:
            if arr[pIndex] == 0:
                i = pIndex
                a = -1
                while i < len(arr):
                    tempA = arr[i]
                    if a > -1:
                        arr[i] = a
                    a = tempA
                    i += 1
                pIndex += 2
            else:
                pIndex += 1
