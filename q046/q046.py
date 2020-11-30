from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def DFS(tem_res):
            if len(tem_res) == len(nums):
                self.result.append(tem_res)
                return
            for item in nums:
                if item in tem_res:
                    continue
                DFS(tem_res + [item])

        DFS([])
        return self.result