class Solution:
    def reverse(self, x: int) -> int:
        tem = x < 0
        x_ = int(str(abs(x))[::-1])
        if tem:
            x_ *= -1
        if x_ not in range(-2**31, 2**31-1):
            return 0
        else:
            return x_