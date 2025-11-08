class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sets = set()
        for s in sentence:
            sets.add(s)
        return len(sets) == 26
