class Solution:
    def reverseDegree(self, s: str) -> int:
        counter = 0
        for i in range(len(s)):
            counter += (26 - (ord(s[i]) - 97)) * (i + 1)
        return counter
