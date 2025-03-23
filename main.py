from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                temp = dict[s[i]]
                dict[s[i]] = i - temp - 1
        for key in dict:
            if distance[ord(key) - 97] != dict[key]:
                return False
        return True
