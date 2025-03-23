from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        for i in range(len(words)):
            currWord = words[i]
            j = i + 1
            while (j < len(words)):
                if self.isPrefixAndSuffix(currWord, words[j]):
                    counter += 1
                j += 1
        return counter

    def isPrefixAndSuffix(self, word1, word2):
        if len(word1) > len(word2):
            return False
        pref = len(word2) - len(word1)
        return True if word2[:len(
            word1)] == word1 and word2[pref:] == word1 else False


s = Solution()
print(s.countPrefixSuffixPairs(["bb", "bb"]))
