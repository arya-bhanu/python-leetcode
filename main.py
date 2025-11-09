from typing import List
import math


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dicts = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dicts:
                arr = []
                arr.append(i)
                dicts[groupSizes[i]] = arr
                continue
            curr = dicts[groupSizes[i]]
            curr.append(i)
            dicts[groupSizes[i]] = curr
        result = []
        for key in dicts:
            if len(dicts[key]) > key:
                length_total = len(dicts[key])
                loop = math.ceil(length_total / key)
                for i in range(loop):
                    if length_total >= key:
                        result.append(dicts[key][i * key : (i * key + key)])
                        length_total -= key
                        continue
                    result.append(
                        dicts[key][len(dicts[key]) - length_total : len(dicts[key])]
                    )
                continue
            result.append(dicts[key])
        return result


sol = Solution()
print(sol.groupThePeople([2, 1, 3, 3, 3, 3, 3, 3, 3, 2]))
