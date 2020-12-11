from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1:
            return 0
        maxProfit = 0
        buy = 0
        for sell in range(len(prices)):
            if prices[buy] <= prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
                continue
            buy = sell

        return maxProfit