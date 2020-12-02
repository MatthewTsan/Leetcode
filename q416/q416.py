from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        if sum(nums) % 2 != 0:
            return False

        subset = int(sum(nums) / 2)
        result = [False for _ in range(subset + 1)]
        result[0] = True
        for i in range(len(nums)):
            for j in range(subset, -1, -1):
                if j < nums[i]:
                    result[j] = result[j]
                else:
                    result[j] = result[j - nums[i]] or result[j]
            # print(result)

        return result[-1]

    # DFS approach: timeout
    def canPartition_DFS(self, nums: List[int]) -> bool:

        def DFS(index, sumNums):
            if index == len(nums):
                if sumNums == sum(nums) / 2:
                    return True
                else:
                    return False
            resultWithNumi = DFS(index + 1, sumNums + nums[index])
            resultWithoutNumi = DFS(index + 1, sumNums)
            return resultWithNumi or resultWithoutNumi

        return DFS(0, 0)