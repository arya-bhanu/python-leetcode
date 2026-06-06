from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sets = set()
        dict = {}
        for n in arr:
            if n in dict:
                c = dict[n]
                dict[n] = c + 1
            else:
                dict[n] = 1

        for _, v in dict.items():
            if v in sets:
                return False
            else:
                sets.add(v)
        return True
