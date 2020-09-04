class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        counter = 0
        while True:
            if X == Y:
                return counter
            if X < Y:
                if Y % 2 == 0:
                    counter += 1
                    Y //= 2
                else:
                    counter += 1
                    Y += 1
            else:
                counter += X - Y
                return counter
        return counter

sol = Solution()
print(sol.brokenCalc(1024, 1))