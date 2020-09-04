from typing import List


class Solution:

    def __init__(self):
        self.__phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        self.__ans = []

    def __backtrack(self, digits, k, temStr):
        print("temStr:", temStr)
        if k == len(digits):
            self.__ans.append(temStr)
            return

        for c in self.__phone[digits[k]]:
            temAns = temStr + c
            self.__backtrack(digits, k + 1, temAns)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.__ans
        self.__backtrack(digits, 0, "")
        return self.__ans


sol = Solution()
string = "23"
print(sol.letterCombinations(string))
