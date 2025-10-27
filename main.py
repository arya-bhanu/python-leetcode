class Solution:
    def convertDateToBinary(self, date: str) -> str:
        splitted = date.split("-")
        return self.convertIntoBinaryString(splitted)

    def convertIntoBinaryString(self, strArr: list[str]):
        resultArr = []
        for s in strArr:
            num = int(s)
            res = num
            resultStr = []
            while res != 0:
                rem = res % 2
                res = res // 2
                resultStr.insert(0, rem)
            resultArr.append("".join(map(str, resultStr)))
        return "-".join(resultArr)
