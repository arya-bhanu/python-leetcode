# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def guess(): int
        i = 0
        j = n
        while i <= j:
            m = (i+j) // 2
            if guess(m) == 0:
                return m
            elif guess(m) < 0:
                j = m - 1
            else:
                i = m + 1
        return
