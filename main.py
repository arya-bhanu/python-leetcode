class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        loop = len(s) // 2
        for i in range(loop):
            j = len(s) - i - 1
            if s[i] != s[j]:
                if ord(s[j]) < ord(s[i]):
                    s[i] = s[j]
                else:
                    s[j] = s[i]
        return "".join(s)
