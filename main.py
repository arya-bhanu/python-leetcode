from typing import List

# others solution


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        c_index_in_s = []

        # Create a list of index c in s
        for i in range(len(s)):
            if s[i] == c:
                c_index_in_s.append(i)

        answer = []
        c_index = 0
        for i in range(len(s)):
            # if it is c add 0
            if s[i] == c:
                answer.append(0)
                c_index += 1
            # If it is first element of c in s
            elif i < c_index_in_s[0]:
                answer.append(c_index_in_s[0] - i)
            # If it is last element of c in s
            elif i > c_index_in_s[-1]:
                answer.append(i - c_index_in_s[-1])
            # If it is in the middle use minimum
            else:
                # find minimum distance between i is before value of current c index and i after 1 before current c index
                answer.append(
                    min((c_index_in_s[c_index] - i), (i - c_index_in_s[c_index - 1])))
        return answer
