from typing import List

# use two pointers


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []

        def prefixsum(arr: List[int]) -> List[int]:
            prev = 0
            res = []
            res.append(prev)
            for i in range(len(arr) - 1):
                calc = arr[i] + prev
                res.append(calc)
                prev = calc
            return res

        def suffixsum(arr: List[int]) -> List[int]:
            prev = 0
            res = []
            res.append(prev)
            for i in range(len(arr) - 1, 0, -1):
                calc = arr[i] + prev
                res.append(calc)
                prev = calc
            return res[::-1]

        prefixed = prefixsum(nums)
        suffixed = suffixsum(nums)

        if (len(prefixed) == len(suffixed)):
            for i in range(len(prefixed)):
                result.append(abs(prefixed[i] - suffixed[i]))

        return result
