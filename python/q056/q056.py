import random
from typing import List


class Solution:
    def qsort(self, list, left, right):
        i = left
        mid = list[left]
        for j in range(left, right):
            if list[j] < mid:
                i += 1
                tem = list[j]
                list[j] = list[i]
                list[i] = tem
        tem = list[left]
        list[left] = list[i]
        list[i] = tem
        if left<i:
            # print(list, left, right, "left", sep="\t")
            self.qsort(list, left, i)
        if i < right - 1:
            # print(list, left, right, "right", sep="\t")
            self.qsort(list, i+1, right)


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while(i < len(intervals) - 1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
                del(intervals[i+1])
                continue
            i += 1

if __name__ == '__main__':
    sol = Solution()
    list = [[1, 4], [2, 3]]
    sol.merge(list)
    print(list)


