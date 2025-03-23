from typing import List

from collections import Counter
# XOR operator, so powerful
# anyting XOR with 0 will be that own value
# anything XOR with itself (same value) will be 0
# XOR is accosiative a ^ (b ^ c) == a ^ b ^ c == (a ^ b) ^ c


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            x = x ^ i
        return x
