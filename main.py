from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # left node, will run first until base case
            subset.append(nums[i])
            dfs(i + 1)
            # right node
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
