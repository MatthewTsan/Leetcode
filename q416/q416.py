from typing import List


class Solution:

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