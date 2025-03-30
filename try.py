from typing import List


def search(nums: List[int], target: int) -> bool:
    nums.sort()
    i = 0
    j = len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] == target:
            return True
        elif nums[m] > target:
            j = m - 1
        else:
            i = m + 1
    return False


nums = [2, 10, 1, 2, 3, 5, 10]

print(search(nums, 0))
