from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        L, R, result = [1] * N, [1] * N, [1] * N
        L[0] = nums[0]
        for i in range(1, N):
            L[i] = L[i - 1] * nums[i]

        R[N - 1] = nums[N - 1]
        for i in range(N - 2, -1, -1):
            R[i] = R[i + 1] * nums[i]

        result[0] = R[1]
        result[-1] = L[-2]
        print(L)
        print(R)
        for i in range(1, N - 1):
            result[i] = L[i - 1] * R[i + 1]

        return result
