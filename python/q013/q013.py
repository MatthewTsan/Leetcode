class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                result += symbols[s[i]]
                break
            if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                result += symbols[s[i + 1]] - symbols[s[i]]
                i += 2
            elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                result += symbols[s[i + 1]] - symbols[s[i]]
                i += 2
            elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                result += symbols[s[i + 1]] - symbols[s[i]]
                i += 2
            else:
                result += symbols[s[i]]
                i += 1
        return result
