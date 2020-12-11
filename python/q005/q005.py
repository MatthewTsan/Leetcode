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

        result = {'max_len': 0,
                  'str': []}
        matrix = [[False for j in range(len(s))] for i in range(len(s))]

        # def print_matrix(m):
        #     for i in range(len(s)):
        #         print(m[i])
        #     print()

        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                # print(i,j, sep=",")
                if i == j:
                    # print(1)
                    matrix[i][j] = True
                elif i == j-1:
                    # print(2)
                    # print(s[i], s[j])
                    matrix[i][j] = s[i] == s[j]
                else:
                    # print(3)
                    if i == len(s)-1 or j == 0:
                        # print(3.1)
                        matrix[i][j] = s[i] == s[j]
                    else:
                        # print(3.2)
                        # print(matrix[i+1][j-1])
                        # print(s[i], s[j], sep=" ")
                        matrix[i][j] = (matrix[i+1][j-1] and s[i] == s[j])


                if matrix[i][j]:
                    if result['max_len'] < j-i+1:
                        result['max_len'] = j-i+1
                        result['str'] = [i,j+1]
            # print_matrix(matrix)
            # print()
        return s[result['str'][0]: result['str'][1]]




    def longestPalindrome(self, s: str) -> str:
        result = self.__solution_2(s)
        return result

