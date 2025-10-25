from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
        val = 0
        for opr in operations:
            val += ops[opr]
        return val
