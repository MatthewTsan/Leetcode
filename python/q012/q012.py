from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, item in enumerate(nums[:-2]):
            if item > 0:
                break
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            bg = index + 1
            ed = len(nums) - 1
            while bg < ed:
                if nums[index] + nums[bg] + nums[ed] == 0:
                    result.append([nums[index], nums[bg], nums[ed]])
                    bg += 1
                    while nums[bg] == nums[bg - 1] and bg < ed:
                        bg += 1
                    ed -= 1
                    while nums[ed] == nums[ed + 1] and bg < ed:
                        ed -= 1
                else:
                    if nums[index] + nums[bg] + nums[ed] < 0:
                        bg += 1
                    else:
                        ed -= 1
        return result
