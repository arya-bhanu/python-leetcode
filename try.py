import bisect
from typing import List


arr = [2, 3, 4, 5, 10, 8]


def bin_search(arr: List[int], target: int) -> bool:
    arr.sort()
    index = bisect.bisect_left(arr, target)
    if index != len(arr) and arr[index] == target:
        return True
    return False


print(bin_search(arr, 2))
