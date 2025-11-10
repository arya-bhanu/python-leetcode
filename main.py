class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_found = False
        counter = 0
        for i in range(len(s) - 1, -1, -1):
            # stopper
            if ord(s[i]) == 32 and is_found:
                break
            if ord(s[i]) == 32 and not is_found:
                continue
            is_found = True
            counter += 1
        return counter
