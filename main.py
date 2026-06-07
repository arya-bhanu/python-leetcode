class Solution:
    def maxDistinct(self, s: str) -> int:
        sets = set()
        for c in s:
            sets.add(c)
        return len(sets)
