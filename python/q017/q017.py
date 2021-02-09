from collections import deque
from typing import List


class Solution_BFS:
    def letterCombinations(self, digits: str) -> List[str]:
        mapList = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ans = deque()
        if len(digits) == 0:
            return ans
        for c in mapList[digits[0]]:
            ans.append(c)
        ## BFS
        for i in range(1, len(digits)):
            N = len(ans[0])
            num = digits[i]
            while len(ans[0]) == N:
                s = ans.popleft()
                for c in mapList[num]:
                    ans.append(s + c)
            print(ans)
        return ans

class Solution_DFS:

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


sol = Solution_BFS()
string = "23"
print(sol.letterCombinations(string))
