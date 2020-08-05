class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = list(num)
        if len(nums) == k:
            return "0"
        for times in range(k):
            i = 1
            while(i < len(nums)):
                if nums[i-1] > nums[i]:
                    nums.pop(i-1)
                    break
                i += 1
            # print(len(nums), len(num), times)
            if len(nums) == len(num) - times:
                del(nums[-1])
            # print(nums)

        while len(nums) > 1 and nums[0] == "0":
            nums.pop(0)
        return "".join(nums)

sol = Solution()
num = "000203040"
k = 3
print(sol.removeKdigits(num, k))