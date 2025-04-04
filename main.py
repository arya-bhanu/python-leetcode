# easy using hashmap
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        dict1 = {}
        dict2 = {}
        sets = set([])
        for i in range(len(word1)):
            dict1[word1[i]] = dict1.get(word1[i], 0) + 1
            dict2[word2[i]] = dict2.get(word2[i], 0) + 1
            if word1[i] not in sets:
                sets.add(word1[i])
            if word2[i] not in sets:
                sets.add(word2[i])
        while len(sets) > 0:
            check = sets.pop()
            if abs(dict1.get(check, 0) - dict2.get(check, 0)) > 3:
                return False
        return True
