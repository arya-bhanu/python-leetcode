import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sumArr = [sum(x) for x in mat]
        HEAP = []
        for i in range(len(sumArr)):
            heapq.heappush(HEAP, (sumArr[i], i))
        return [heapq.heappop(HEAP)[1] for _ in range(k)]
