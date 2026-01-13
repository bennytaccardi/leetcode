from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        max = 0
        for idx in range(1, len(prices)):
            price = prices[idx]
            possible_profit = price - current
            max = possible_profit if possible_profit > 0 and possible_profit > max else max
            if price < current:
                current = price
        return max

s= Solution()
print(s.maxProfit([7,6,4,3,1]))
