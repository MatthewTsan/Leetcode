class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        a = len(s) // (2 * numRows - 2)

        result = ""
        for i in range(numRows):
            for j in range(a+1):
                if j * (2 * numRows - 2) + i < len(s):
                    result += s[j * (2 * numRows - 2) + i]
                if i != 0 and i != numRows - 1 and (j + 1) * (2 * numRows - 2) - i < len(s):
                    result += s[(j + 1) * (2 * numRows - 2) - i]
        return result
