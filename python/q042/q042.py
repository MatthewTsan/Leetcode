from collections import deque
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque()
        ans = 0
        for i in range(len(height)):
            h = height[i]
            while stack and height[stack[-1]] < h:
                # pop the top one and calculate water between i and stack[-1] (not i between top)
                top = stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                    continue
                distance = i - stack[-1] - 1
                ans += distance * (min(height[stack[-1]], h) - height[top])
                print(i, top, ans)
            stack.append(i)
        return ans
