from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = nums[0]
        minNum = nums[0]
        res = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxNum, minNum = minNum, maxNum
            maxNum = max(num, maxNum * num)
            minNum = min(num, minNum * num)
            res = max(res, maxNum)
            # print(maxNum, minNum, res, sep=" ")
        return res

if __name__ == '__main__':
    sol = Solution()
    list = [2, 3, -2, 4]
    res = sol.maxProduct(list)
    print(res)