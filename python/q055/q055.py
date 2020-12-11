from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        jump = [False for i in range(len(nums))]
        jump[0] = True
        for i, item in enumerate(nums):
            if not jump[i]:
                continue
            for j in range(i, i+item+1):
                if j < len(nums):
                    jump[j] = True
        return jump[-1]

    def canJump_greedy(self, nums: List[int]) -> bool:
        max_jump = 0
        for i, length in enumerate(nums):
            if max_jump < i:
                break
            max_jump = max(max_jump, i + length)
        print(max_jump)
        return max_jump+1 >= len(nums)



sol = Solution()
list = [3,2,1,0,4]
ans = sol.canJump_greedy(list)
print(ans)