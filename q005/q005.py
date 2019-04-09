class Solution:
    def __solution_1(self, s):
        if s == '':
            return ''
        result = []
        max_len = 0
        for i in range(0, len(s)):
            j = 0
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                j += 1
            j -= 1

            if max_len <  2 * j + 1:
                max_len = 2 * j + 1
                result = [i-j, i+j+1]

            j = 0
            while i-j >= 0 and i+j+1 < len(s) and s[i-j] == s[i+j+1]:
                j += 1

            if max_len < 2 * j:
                max_len = 2 * j
                result = [i-j+1, i+j+1]

        return s[result[0]:result[1]]

    def __solution_2(self, s):

        if s == "":
            return ""

        matrix_len = len(s) + 1
        matrix = [[False for j in range(matrix_len)] for i in range(len(s))]
        matrix.append([True for _ in range(matrix_len)])
        for i in range(matrix_len):
            matrix[i][i] = True
            matrix[i][0] = True

        def print_matrix(m):
            for i in range(matrix_len):
                print(m[i])

        for i in reversed(range(len(s))):
            for j in range(len(s)):
                j = j + 1
                print(i, j)
                if i == j+1:
                    matrix[i][j] = s[i] == s[j]
                elif i < j - 1:
                    matrix[i][j] = matrix[i+1][j-1] and s[i] == s[j] # out of range
            print(i, j, sep=",")
            print_matrix(matrix)




    def longestPalindrome(self, s: str) -> str:
        result = self.__solution_2(s)
        return result

