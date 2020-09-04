class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        while left < right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1

sol = Solution()
print(sol.mySqrt(25))