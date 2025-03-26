from typing import List

# naive use bruteforce


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices) - 1):
            j = i + 1
            for x in range(j, len(prices)):
                if prices[x] <= prices[i]:
                    prices[i] = prices[i] - prices[x]
                    break
        return prices
