from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        sets = set()
        o = []
        for i in friends:
            sets.add(i)
        for ord in order:
            if ord in sets:
                o.append(ord)
        return o
