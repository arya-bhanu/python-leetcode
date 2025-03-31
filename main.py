from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        for q in queries:
            max = 0
            for i in range(len(nums)):
                if sum(nums[0:i+1]) <= q:
                    temp = len(nums[0:i+1])
                    if temp > max:
                        max = temp
            res.append(max)
        return [0] if len(res) == 0 else res
