from typing import List

# naive approach using substring principle


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        length = len(words)
        for i in range(length):
            for j in range(i + 1, length):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    counter += 1
        return counter

    def isPrefixAndSuffix(self, word1, word2):
        if len(word1) > len(word2):
            return False
        pref = len(word2) - len(word1)
        return True if word2[:len(
            word1)] == word1 and word2[pref:] == word1 else False


s = Solution()
print(s.countPrefixSuffixPairs(["bb", "bb"]))
