from typing import List

# solved with my own solution


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        diff = None
        arr.sort()
        for i in range(len(arr) - 1):
            if diff is None:
                diff = arr[i + 1] - arr[i]
                continue
            if arr[i + 1] - arr[i] != diff:
                return False
        return True
