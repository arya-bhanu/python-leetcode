from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        result = []
        if len(A) == len(B):
            counter = 0
            prev = 0
            for i, a in enumerate(A):
                if a in seen:
                    counter = counter + 1
                else:
                    seen.add(a)

                if B[i] in seen:
                    counter = counter + 1
                else:
                    seen.add(B[i])
                if len(result) > 0:
                    prev = result[-1]
                result.append(prev + counter)
                counter = 0
        return result
