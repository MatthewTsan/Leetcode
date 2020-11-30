from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        busket = [False for item in nums]
        for item in nums:
            if busket[item]:
                return item
            else:
                busket[item] = True
