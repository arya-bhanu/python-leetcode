from typing import List


# naive ways
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []

        def sumNext(i: int):
            sum = 0
            for i in range(i + 1, i + k + 1):
                if i < len(code):
                    sum += code[i]
                else:
                    sum += code[i - len(code)]
            return sum

        if k == 0:
            return [0] * len(code)
        if k > 0:
            for i in range(len(code)):
                res.append(sumNext(i))
        else:
            for i in range(len(code)):
                sum = 0
                for j in range(1, abs(k) + 1):
                    sum += code[i - j]
                res.append(sum)
        return res
