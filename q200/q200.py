from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def DFS(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if visited[i][j]:
                return
            if grid[i][j] != "1":
                return

            # print(i, j)
            visited[i][j] = True

            DFS(i - 1, j)
            DFS(i, j - 1)
            DFS(i + 1, j)
            DFS(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    result += 1
                    DFS(i, j)

        return result

if __name__ == '__main__':
    solution = Solution()
    list = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    result = solution.numIslands(list)
    print(result)