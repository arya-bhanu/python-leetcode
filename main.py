from typing import List

# traditional way, using two pointers


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ""
        for word in words:
            if self.isPalindrome(word):
                answer = word
                break
        return answer

    def isPalindrome(self, word: str) -> bool:
        j = len(word) - 1
        for i in range(len(word) // 2):
            if word[i] != word[j]:
                return False
            j -= 1
        return True
