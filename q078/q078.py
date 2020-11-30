from typing import List


class Solution:
    def __init(self):
        self.__result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = [[]]

        # def DFS(tem_res):
        #     if len(tem_res) > len(nums):
        #         return
        #     self.result.append(tem_res)
        #     for item in nums:
        #         if item in tem_res:
        #             continue
        #         DFS(tem_res + [item])

        def DFS(tem_res, index):
            if len(tem_res) > len(nums):
                return
            self.result.append(tem_res)
            # print(tem_res, index, nums[index:])
            for i, item in enumerate(nums[index:]):
                DFS(tem_res + [item], i + index + 1)

        for i, item in enumerate(nums):
            DFS([item], i + 1)

        return self.result