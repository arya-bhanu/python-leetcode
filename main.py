from typing import List


class Solution:
    # greedy solution
    def countKDifference(self, nums: List[int], k: int) -> int:
        # using hashmap
        hash_map = {}
        counter = 0
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
                continue
            curr = hash_map[num]
            curr += 1
            hash_map[num] = curr
        for hash_num in hash_map:
            if hash_num - k in hash_map:
                counter += hash_map[hash_num] * hash_map[hash_num - k]
        return counter
