

from typing import List


# count digits length without convert into strings

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            if self.countDigitNumber(num) % 2 == 0:
                counter += 1
        return counter

    def countDigitNumber(self, n) -> int:
        if n == 0:
            return 1
        length = 0
        while n != 0:
            n = n // 10
            length += 1
        return length
