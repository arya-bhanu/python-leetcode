from typing import List


arr = [1, 2, 3, 4, 5]
arr2 = [1, 2]


def shift(arr: List[int]):
    prev = 0
    for i in range(len(arr)):
        temp = arr[i]
        arr[i] = prev
        prev = temp


shift(arr)
print(arr)
