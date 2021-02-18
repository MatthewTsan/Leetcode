from collections import defaultdict


class Solution:
    def __init__(self):
        self.map = defaultdict(int)

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1 or n == -1:
            return x if n == 1 else 1 / x

        if n in self.map:
            return self.map[n]
        mid = int(n / 2)
        self.map[n] = self.myPow(x, mid) * self.myPow(x, n - mid)
        # print(n, self.map, self.map[n])
        return self.map[n]
