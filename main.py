from typing import List

# naive iteration
# very slow


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dist = []
        res = []
        for i in range(len(s)):
            if s[i] == c:
                dist.append(i)
        for i in range(len(s)):
            min = -1
            for j in dist:
                absVal = abs(j - i)
                if min == -1:
                    min = absVal
                if absVal < min:
                    min = absVal
            res.append(min)
        return res
