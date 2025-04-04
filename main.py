# using bruteforce
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count_valid = 0
        for i in range(len(s)):
            j = i
            counterOne, counterZero = 0, 0
            while j < len(s):
                if s[j] == "1":
                    counterOne += 1
                else:
                    counterZero += 1
                j += 1

                if counterOne <= k or counterZero <= k:
                    count_valid += 1

        return count_valid
