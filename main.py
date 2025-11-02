from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = 0
        nums1.sort()
        nums2.sort()
        for num1 in nums1:
            for num2 in nums2:
                calc = num2 * k
                if calc > num1:
                    break
                elif num1 % calc == 0:
                    pair += 1
        return pair
