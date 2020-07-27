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

if __name__ == '__main__':
    sol = Solution()
    list = "11110"
    res = sol.numDecodings(list)
    print(res)