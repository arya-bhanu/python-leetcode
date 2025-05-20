from typing import List

# works now


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = []
        for i in range(len(pref)):
            if i == 0:
                res.append(pref[0])
                continue
            j = i - 1
            res.append(pref[i] ^ pref[j])
        return res
