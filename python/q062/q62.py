class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        list = [[1 for i in range(m)] for j in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                list[i][j] = list[i-1][j] + list[i][j-1]
        # print(list)
        return list[n-1][m-1]

if __name__ == '__main__':
    solution = Solution()
    res = solution.uniquePaths(3, 2)
    print(res)