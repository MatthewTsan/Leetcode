from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minP = prices[0]
        ans = 0
        for p in prices:
            minP = min(minP, p)
            ans = max(ans, p - minP)
        return ans


class Solution2:
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