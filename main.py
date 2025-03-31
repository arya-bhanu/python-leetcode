from typing import List

# naive ways
# time limit


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        sets = set(arr)
        counter = 0
        i = 1
        while (counter is not k):
            if i not in sets:
                counter += 1
            i += 1
        return i - 1
