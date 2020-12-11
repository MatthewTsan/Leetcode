from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # print(nums)
        if len(nums) <= 1:
            return len(nums)
        if len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2

        i = 1
        ans = 1
        while i < len(nums) and nums[i - 1] == nums[i]:
            i += 1

        if i == len(nums):
            return ans
        isIncrease = nums[i-1] < nums[i]
        ans += 1
        i += 1

        # print(ans)
        while i < len(nums):
            # print(i, isIncrease, nums[i-1] < nums[i])
            if nums[i - 1] == nums[i] or isIncrease == (nums[i - 1] < nums[i]):
                i += 1
            else:
                isIncrease = nums[i - 1] < nums[i]
                ans += 1
                i += 1
            # print(ans)

        return ans


sol = Solution()
list = [0, 0, 1, 1, 1, 3, 2]
print(sol.wiggleMaxLength(list))
