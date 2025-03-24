class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stacks = list(word)
        str = ""
        has = False
        for c in word:
            str += stacks.pop(0)
            if c == ch:
                has = True
                break
        result = str[::-1] + ''.join(stacks)
        return result if has else str
