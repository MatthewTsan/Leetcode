from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        intMaxArea = 0
        while i < j:
            h = min(height[i], height[j])
            intMaxArea = max(intMaxArea, h * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return intMaxArea


if __name__ == '__main__':
    solution = Solution()
    list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = solution.maxArea(list)
    print(res)
