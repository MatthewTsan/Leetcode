from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        matrix = [0 if obstacleGrid[0][0] == 1 else 1]
        for i in range(1, n):
            matrix.append(0 if (obstacleGrid[0][i] == 1 or matrix[i - 1] == 0) else 1)

        print(matrix)
        for i in range(1, m):
            matrix[0] = 0 if obstacleGrid[i][0] == 1 or matrix[0] == 0 else 1
            for j in range(1, n):
                matrix[j] = 0 if obstacleGrid[i][j] == 1 else matrix[j - 1] + matrix[j]
            print(matrix)

        return matrix[-1]