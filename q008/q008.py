class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str:
            return 0
        eng = 1
        result = 0
        if str[0] == "+":
            eng = 1
            str = str[1:]
        elif str[0] == "-":
            eng = -1
            str = str[1:]
        p = 0
        while p < len(str) and str[p].isdigit():
            result = result * 10 + int(str[p])
            print("s:", str[p], "re:", result)
            p += 1

        result = eng * result
        if result > 2**31-1:
            result = 2**31-1
        if result < -2**31:
            result = -2**31
        return result
