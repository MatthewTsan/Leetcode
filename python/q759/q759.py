# Definition for an Interval.
import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end



class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ans = []
        heap = []
        for person in schedule:
            for interval in person:
                heapq.heappush(heap, (interval.start, interval.end))

        start = 0
        while heap:
            job = heapq.heappop(heap)
            start = job[1]
            while heap and heap[0][1] <= start:
                heapq.heappop(heap)
            if heap and heap[0][0] > start:
                ans.append(Interval(start, heap[0][0]))

        return ans