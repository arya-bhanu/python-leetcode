class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split(" ")
        res = ''
        for i in range(len(splited)):
            splited[i] = splited[i][::-1]
            if i != len(splited) - 1:
                res += f"{splited[i]} "
            else:
                res += splited[i]
        return res
