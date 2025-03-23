from typing import List
import copy


def generate(numRows: int) -> List[List[int]]:
    storedArr = [[1], [1, 1]]
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return storedArr
    nLoop = numRows - 2
    for x in range(nLoop):
        resArr = []
        resArr.append(1)
        i = 0
        j = i + 1
        while j < len(storedArr[x+1]):
            resArr.append(storedArr[x+1][i] + storedArr[x+1][j])
            i += 1
            j += 1
        resArr.append(1)
        storedArr.append(resArr)
    return storedArr


print(generate(5))
