from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        max = len(s)
        min = 0
        res = []
        for schr in s:
            if schr == "I":
                res.append(min)
                min += 1
                continue
            if schr == "D":
                res.append(max)
                max -= 1
        if s[len(s) - 1] == "D":
            res.append(min)
        if s[len(s) - 1] == "I":
            res.append(max)
        return res
