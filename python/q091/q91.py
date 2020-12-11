class Solution:
    def numDecodings(self, s: str) -> int:
        cache = []
        if s[0] == "0":
            cache.append(0)
        else:
            cache.append(1)
        if len(s) == 1:
            return cache[-1]

        if int(s[0:1]) <= 26 and int(s[0:1]) >= 10:
            cache.append(2)
        else:
            cache.append(1)

        for i in range(2, len(s) + 1):
            cache.append(0)
            if s[i-1] != "0":
                cache[i] += cache[i-1]
            if s[i-2] != "0" and 10 <= int(s[i-2: i]) <= 26:
                cache[i] += cache[i-2]
        return cache[-1]


class Solution_2:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        def canCombine(s, i):
            if i < 1:
                return False
            if s[i - 1] == "0":
                return False
            num = int(s[i - 1] + s[i])
            if num > 26:
                return False
            return True

        if len(s) == 1:
            return 1

        result = [1]
        if s[1] == "0":
            if canCombine(s, 1):
                result.append(1)
            else:
                return 0
        elif canCombine(s, 1):
            result.append(2)
        else:
            result.append(1)

        i = 2
        while (i < len(s)):
            if s[i] == "0":
                if canCombine(s, i):
                    result.append(result[i - 2])
                else:
                    return 0
            elif canCombine(s, i):
                result.append(result[i - 1] + result[i - 2])
            else:
                result.append(result[i - 1])

            i += 1

        return result[-1]

if __name__ == '__main__':
    sol = Solution()
    list = "11110"
    res = sol.numDecodings(list)
    print(res)