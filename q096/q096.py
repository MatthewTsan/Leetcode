class Solution:
    res = {}

    def findNums(self, bg, ed):
        if ed - bg == 0:
            self.res[(bg, ed)] = 1
            return 1
        if ed - bg == 1:
            self.res[(bg, ed)] = 1
            return 1
        if (bg, ed) in self.res:
            return self.res[(bg, ed)]
        sum = 0
        for i in range(bg, ed):
            sum += self.findNums(bg, i) * self.findNums(i + 1, ed)
        self.res[(bg, ed)] = sum
        return sum

    def numTrees(self, n: int) -> int:
        if n == 0:
            return 0
        self.findNums(1, n + 1)
        return self.res[(1, n + 1)]

