from typing import List


# naive
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)

        # go right
        for i in range(len(boxes)):
            if boxes[i] == "1" and i != len(boxes) - 1:
                counter = 1
                for j in range(i + 1, len(boxes)):
                    res[j] = res[j] + counter
                    # print(res)
                    counter += 1
        # go left
        for i in range(len(boxes) - 1, -1, -1):
            if boxes[i] == "1" and i != 0:
                counter = 1
                for j in range(i - 1, -1, -1):
                    res[j] = res[j] + counter
                    counter += 1
        return res
