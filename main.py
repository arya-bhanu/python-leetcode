class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        stacks = []
        for c in s:
            count = len(stacks)
            if count > counter:
                counter = count
            if c == "(":
                stacks.append(")")
            elif c == ")":
                if stacks[-1] == ")":
                    stacks.pop()
        return counter
