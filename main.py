# with own solution using prefix
class Solution:
    def pivotInteger(self, n: int) -> int:
        prev = 0
        prefixSum = []
        for i in range(1, n + 1):
            calcPrev = prev + i
            prefixSum.append(calcPrev)
            prev = calcPrev

        post = 0
        for i in range(n, 0, -1):
            calc = post + i
            getVal = prefixSum[i-1]
            if calc == getVal:
                return i
            post = calc
        return -1
