from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dicts = {}
        res = []
        for i in range(len(heights)):
            dicts[heights[i]] = names[i]
        heights.sort(reverse=True)
        for h in heights:
            res.append(dicts[h])
        return res
