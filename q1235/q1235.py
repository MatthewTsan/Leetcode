from time import sleep
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        startSort = [i for i in range(len(startTime))]
        endSort = [i for i in range(len(endTime))]
        startSort.sort(key=lambda x: startTime[x])
        endSort.sort(key=lambda x: endTime[x])
        for x, i in enumerate(startSort):
            print(x, i, startTime[i])
        print()
        for x, i in enumerate(endSort):
            print(x, i, endTime[i])

        sleep(0.1)
        f = [0 for i in range(len(startSort))]
        f[0] = profit[startSort[0]]
        for i in startSort[1:]:
            print(i)
            res = f[i-1]
            k = 0
            while endTime[endSort[k]] <= startTime[i]:
                print(endSort[k])
                print(endTime[endSort[k]], startTime[i])
                res = max(res, f[endSort[k] + profit[endSort[k]]])
                k += 1
            f[i] = res
            print(f)



sol = Solution()
startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]
sol.jobScheduling(startTime, endTime, profit)
