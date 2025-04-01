from typing import List


original = [7]


def prefix(nums: List[int]):
    nums.sort()
    prev = 0
    res = []
    res.append(0)
    for i in range(len(nums)):
        calc = prev + nums[i]
        res.append(calc)
        prev = calc
    return res


prefixed = prefix(original)

i = len(original)

while i >= 0:
    arr = original[i:]
    print(i)
    if sum(arr) > prefixed[i]:
        arr.sort(reverse=True)
        print(arr)
    i -= 1

print(original)
print(prefixed)
