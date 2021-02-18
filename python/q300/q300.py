class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [0 for _ in nums]
        for i in range(len(nums)):
            maxNum = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxNum = max(ans[j], maxNum)
            ans[i] = maxNum + 1
        return max(ans)