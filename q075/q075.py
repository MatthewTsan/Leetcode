from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        contNums = [0, 0, 0]
        for i in nums:
            contNums[i] += 1
        # print(contNums)
        for i in range(contNums[0]):
            nums[i] = 0
        for i in range(contNums[0], contNums[0] + contNums[1]):
            nums[i] = 1
        for i in range(contNums[0] + contNums[1], contNums[0] + contNums[1] + contNums[2]):
            nums[i] = 2

    @staticmethod
    def sortColors_2(nums: List[int]) -> None:
        def swap(i, j):
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem

        i = 0
        j = len(nums) - 1
        k = 0
        while k <= j:
            print(i, j, k, sep=" ", end=" ")
            print(nums)
            if nums[k] == 1 or k < i:
                k += 1
                continue
            if nums[k] == 0:
                swap(k, i)
                i += 1
                continue
            if nums[k] == 2:
                swap(k, j)
                j -= 1
                continue


sol = Solution()
list = [2, 0, 2, 1, 1, 0]
sol.sortColors_2(list)
print(list)
