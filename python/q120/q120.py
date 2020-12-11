from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        dp = [0 for _ in triangle[-1]]
        dp[0] = triangle[0][0]
        print(dp)
        for level in triangle[1:]:
            dp[len(level) - 1] = dp[len(level) - 2] + level[-1]
            for i in range(len(level) - 2, 0, -1):
                dp[i] = min(dp[i - 1], dp[i]) + level[i]

            dp[0] = dp[0] + level[0]

            print(dp)
        return min(dp)

