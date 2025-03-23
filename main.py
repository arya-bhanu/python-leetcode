class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = 0
        isContainOdd = False
        if len(s) == 1:
            return 1
        dict = {}
        for sVal in s:
            if sVal not in dict:
                dict[sVal] = 1
            else:
                temp = dict[sVal]
                temp += 1
                dict[sVal] = temp

        for _, val in dict.items():
            if val % 2 == 0:
                counter += val
            else:
                isContainOdd = True
                counter += (val // 2) * 2
        if isContainOdd:
            counter += 1
        return counter
