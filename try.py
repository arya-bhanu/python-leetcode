from typing import List


# [1,3,4,6,7]
# [1,4,8,14,21]
def prefix(nums: List[int]) -> List[int]:
    nums.sort()
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


prefixed = prefix([4, 5, 2, 1])
print(prefixed)
print(search(prefixed, 5))
