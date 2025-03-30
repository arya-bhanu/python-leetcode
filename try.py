from typing import List


def search(nums: List[int], target: int, d: int) -> List[int]:
    nums.sort()
    res = []
    # counter = 0
    i = 0
    j = len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        absTarget = abs(nums[m] - target)
        if absTarget <= d:
            res.append(absTarget)
        if absTarget < target:
            i = m + 1
            continue
        if absTarget > 0:
            j = m - 1
    return res


nums = [-5, -2, 10, -3, 7]

print(search(nums, 1, 6))
