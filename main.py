from typing import List

# approach using more simple python built-in function (startsWith and endsWith)


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        length = len(words)
        for i in range(length):
            for j in range(i + 1, length):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    counter += 1
        return counter


s = Solution()
print(s.countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]))
