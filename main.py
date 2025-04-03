from typing import List

# easy using bruteforce


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        targetLength = len(s)
        conctStr = ""
        for i in words:
            conctStr += i
            if len(conctStr) > targetLength:
                return False
            if len(conctStr) == targetLength and conctStr == s:
                return True
        return False
