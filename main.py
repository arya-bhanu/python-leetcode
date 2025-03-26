from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [self.flipInvert(x) for x in image]

    def flipInvert(self, arr: List[int]) -> List[int]:
        return [x ^ 1 for x in arr[::-1]]
