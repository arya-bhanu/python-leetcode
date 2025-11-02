class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s) - 1):
            j = i + 1
            total += abs(ord(s[i]) - ord(s[j]))

        return total
