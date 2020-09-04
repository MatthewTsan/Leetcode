from typing import List


class Solution:
    def __init__(self):
        self.__ans = []

    def __backTracking(self, temStr, leftNum, rightNum):
        print(temStr)
        if leftNum == 0 and rightNum == 0:
            self.__ans.append(temStr)
            return

        if leftNum > 0:
            self.__backTracking(temStr + "(", leftNum - 1, rightNum + 1)
        if rightNum > 0:
            self.__backTracking(temStr + ")", leftNum, rightNum - 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.__backTracking("", n, 0)
        return self.__ans


sol = Solution()
print(sol.generateParenthesis(4))