from typing import List


# you can use reverse string in python for checking palindrome
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ""
        for word in words:
            if word == word[::-1]:
                answer = word
                break
        return answer
