from typing import List

# accepted but very slow


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        def isEven(num: int):
            return num % 2 == 0
        for i in range(len(nums)):
            if isEven(i):
                if isEven(nums[i]):
                    continue
                else:
                    j = i + 1
                    while j < len(nums):
                        if isEven(nums[j]):
                            temp = nums[j]
                            nums[j] = nums[i]
                            nums[i] = temp
                            break
                        j += 1
            else:
                if not isEven(nums[i]):
                    continue
                else:
                    j = i + 1
                    while j < len(nums):
                        if not isEven(nums[j]):
                            temp = nums[j]
                            nums[j] = nums[i]
                            nums[i] = temp
                            break
                        j += 1
        return nums
