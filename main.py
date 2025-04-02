from typing import List

# use two pointers


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []

        prefixed = []
        suffixed = []

        prevPref = 0
        postSuff = 0

        prefixed.append(prevPref)
        suffixed.append(postSuff)

        for i in range(len(nums) - 1):
            calcPrev = prevPref + nums[i]
            prefixed.append(calcPrev)
            prevPref = calcPrev

            j = len(nums) - 1 - i
            calcPost = postSuff + nums[j]
            suffixed.append(calcPost)
            postSuff = calcPost

        suffixed = suffixed[::-1]

        if (len(prefixed) == len(suffixed)):
            for i in range(len(prefixed)):
                result.append(abs(prefixed[i] - suffixed[i]))

        return result
