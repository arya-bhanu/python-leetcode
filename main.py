from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_dict = []
        index_dict = {}
        for index, val in enumerate(list1):
            if val not in index_dict:
                index_dict[val] = index

        for index, val in enumerate(list2):
            if val in index_dict:
                sum_index = index + index_dict[val]
                if len(min_dict) > 0:
                    sum_min_dict = min_dict[len(min_dict) - 1]["index_sum"]
                    if sum_index < sum_min_dict:
                        obj = {}
                        obj["index_sum"] = sum_index
                        obj["val"] = val
                        min_dict = [obj]
                    elif sum_index == sum_min_dict:
                        obj = {}
                        obj["index_sum"] = sum_index
                        obj["val"] = val
                        min_dict.append(obj)
                else:
                    obj = {}
                    obj["index_sum"] = sum_index
                    obj["val"] = val
                    min_dict.append(obj)
        results = []
        for obj in min_dict:
            results.append(obj["val"])
        return results
