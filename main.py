from typing import List


class Solution:
    def clearDigits(self, s: str) -> str:
        stacksL: List[str] = []
        stacksR: List[str] = []
        ori = list(s)
        while len(ori) > 0:
            if ori[0].isdigit():
                if len(stacksL) > 0 and not stacksL[-1].isdigit():
                    stacksL.pop()
                    ori.pop(0)
                else:
                    stacksR.append(ori.pop(0))
            else:
                stacksL.append(ori.pop(0))
        return ''.join(stacksL + stacksR)
