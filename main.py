from typing import List


# prefix sum is very good, must learn about it
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()

        def prefix(nums: List[int]) -> List[int]:
            prev = 0
            res = []
            for i in nums:
                calc = i + prev
                res.append(calc)
                prev = calc
            return res

        def search(nums: List[int], target) -> int:
            i = 0
            j = len(nums) - 1
            while i <= j:
                m = (i+j) // 2
                if nums[m] == target:
                    return m + 1
                elif nums[m] < target:
                    i = m + 1
                else:
                    j = m - 1
            return i

        prefixList = prefix(nums)

        for q in queries:
            res.append(search(prefixList, q))
        return res
