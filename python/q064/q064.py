from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = [grid[0][0]]
        for i in range(1, len(grid[0])):
            cache.append(cache[i - 1] + grid[0][i])
        print(cache)
        for i in range(1, len(grid)):
            cache[0] = cache[0] + grid[i][0]
            for j in range(1, len(grid[0])):
                cache[j] = min(cache[j - 1] + grid[i][j], cache[j] + grid[i][j])
            print(cache)
        return cache[-1]


if __name__ == '__main__':
    sol = Solution()
    list = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    res = sol.minPathSum(list)
    print(res)
