from typing import List

# use naive approach


def buildArray(nums: List[int]) -> List[int]:
    container = []
    for i in range(len(nums)):
        container.append(nums[nums[i]])
    return container


print(buildArray([0, 2, 1, 5, 3, 4]))
