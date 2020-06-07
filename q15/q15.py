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

            while(i < j):
                if nums[i] + nums[j] == target:
                    result.append([item, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1]:
                        i += 1
                        if i >= len(nums):
                            break
                    while nums[j] == nums[j+1]:
                        j -= 1
                        if j <= index:
                            break
                else:
                    if nums[i] + nums[j] < target:
                        i += 1
                    else:
                        j -= 1
        return result

if __name__ == '__main__':
    so = Solution()
    arr = [0, 0, 0]
    res = so.threeSum(arr)
    print(res)