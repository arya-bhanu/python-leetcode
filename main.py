from typing import List

# naive ways
# time limit


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        first = arr[0]

        # opening
        if first is not 1:
            if first - 1 >= k:
                return k
            else:
                k -= first - 1
        for i in range(len(arr) - 1):
            j = i + 1
            diff = arr[j] - arr[i] - 1
            if diff > 0:
                if k - diff > 0:
                    k -= diff
                else:
                    return arr[i] + k

        # closing
        if k > 0:
            return arr[-1] + k
        return
