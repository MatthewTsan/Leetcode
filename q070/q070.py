class Solution:
    def climbStairs(self, n: int) -> int:
        F = []
        F.append(1)
        F.append(2)
        if n < 3:
            return F[n - 1]

        for i in range(2, n):
            F.append(F[i - 1] + F[i - 2])

        return F[n - 1]