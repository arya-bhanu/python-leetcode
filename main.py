from typing import List


# naive, brute force approach
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [x for x in range(len(nums)) if nums[x] == target]
