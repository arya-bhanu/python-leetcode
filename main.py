from typing import List


# [1,0,2,3,0,4,5,0]
# [1,0,0,2,3,0,4,5]
# [1,0,0,2,3,0,0,4]

class Solution:
    def duplicateZeros(self, arr: List[int]):
        for i in range(len(arr) - 1):
            if arr[i] == 0:
                prev = 0
                for x in range(i, len(arr)):
                    print(x)
                    temp = arr[x]
                    arr[x] = prev
                    prev = temp
        return arr

    def shift(self, arr: List[int]):
        prev = 0
        for i in range(len(arr)):
            temp = arr[i]
            arr[i] = prev
            prev = temp
