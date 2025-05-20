from typing import List

# works but time limit execeded


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        for i in range(len(pref)):
            if i == 0:
                res.append(pref[0])
            else:
                finalOp = pref[i]
                for op in res:
                    finalOp = finalOp ^ op
                res.append(finalOp)
        return res
