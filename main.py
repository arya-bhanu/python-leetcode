from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        loop = n // 2
        i = 1
        res = []
        while i <= loop:
            res.append(i)
            res.append(-i)
            i += 1
        if n % 2 != 0:
            res.append(0)
        return res
