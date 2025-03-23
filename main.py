from typing import List

# you can use filter like, or map like equivalent with list comprehension in python


# in js
# function buildArray(nums){
#     return nums.map((_,index)=>nums[nums[index]])
# }

def buildArray(nums: List[int]) -> List[int]:
    return [nums[nums[x]] for x in range(len(nums))]


print(buildArray([0, 2, 1, 5, 3, 4]))
