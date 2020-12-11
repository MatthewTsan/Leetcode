from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, item in enumerate(nums[:-2]):
            if item > 0:
                break
            if item == nums[index - 1] and index > 0:
                continue
            target = 0 - item
            i = index + 1
            j = len(nums) - 1

            while (i < j):
                if nums[i] + nums[j] == target:
                    result.append([item, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1]:
                        i += 1
                        if i >= len(nums):
                            break
                    while nums[j] == nums[j + 1]:
                        j -= 1
                        if j <= index:
                            break
                else:
                    if nums[i] + nums[j] < target:
                        i += 1
                    else:
                        j -= 1
        return result


class Solution_SecondTry:
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


if __name__ == '__main__':
    so = Solution()
    arr = [0, 0, 0]
    res = so.threeSum(arr)
    print(res)
