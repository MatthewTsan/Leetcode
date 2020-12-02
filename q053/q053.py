from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            maxSub = max(nums[i], maxSub + nums[i])
            result = max(result, maxSub)
            # print(maxSub, result, sep=" ")
        return result


class Solution_2:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = nums[0]
        preResult = 0
        for i in range(len(nums)):
            if preResult < 0:
                preResult = nums[i]
            else:
                preResult += nums[i]

            result = max(preResult, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(list)
    print(result)
