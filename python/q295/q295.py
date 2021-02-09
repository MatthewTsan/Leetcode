import heapq



class MedianFinder:
    minHeap = []
    maxHeap = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addMaxHeap(self, num):
        heapq.heappush(self.maxHeap, -num)

    def popMaxHeap(self):
        return -heapq.heappop(self.maxHeap)

    def getMaxHeap(self):
        return -self.maxHeap[0]

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= self.getMaxHeap():
            self.addMaxHeap(num)
        else:
            heapq.heappush(self.minHeap, num)
        if len(self.maxHeap) < len(self.minHeap):
            self.addMaxHeap(heapq.heappop(self.minHeap))
        if len(self.maxHeap) - len(self.minHeap) == 2:
            heapq.heappush(self.minHeap, self.popMaxHeap())

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (self.getMaxHeap() + self.minHeap[0]) / 2.0
        return self.getMaxHeap()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()