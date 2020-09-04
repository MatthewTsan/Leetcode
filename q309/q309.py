from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        print("price\t", prices, end="\n\n")
        sell = [0 for _ in range(len(prices))]
        buy = [0 for _ in range(len(prices))]
        cool = [0 for _ in range(len(prices))]

        for i in range(1, len(prices)):
            for j in range(0, i - 1):
                buy[i] = max(buy[i], sell[j])
            for j in range(0, i):
                sell[i] = max(sell[i], buy[j] + (prices[i] - prices[j]))
            cool[i] = sell[i - 1]
            print("buy:\t", buy)
            print("sell:\t", sell)
            print("cool\t", cool, end="\n\n")

        return max(sell[-1], buy[-1], cool[-1])


sol = Solution()
list = []
print(sol.maxProfit(list))
