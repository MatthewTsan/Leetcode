import heapq
from collections import defaultdict


class Solution:
    def reorganizeString(self, S: str) -> str:
        map = defaultdict()
        maxHeap = []

        def pushHeap(c):
            heapq.heappush(maxHeap, (-map.get(c, 0), c))

        def popHeap():
            return heapq.heappop(maxHeap)[1]

        def getHeap():
            return maxHeap[0][1]

        for c in S:
            map[c] = map.get(c, 0) + 1

        for key in map:
            pushHeap(key)
            if map.get(key) > (len(S) + 1) / 2:
                return ""

        ans = ""
        while len(maxHeap) >= 2:
            c1 = popHeap()
            c2 = popHeap()
            ans = ans + c1 + c2
            map[c1] = map.get(c1, 0) - 1
            map[c2] = map.get(c2, 0) - 1
            if map.get(c1, 0) != 0:
                pushHeap(c1)
            if map.get(c2, 0) != 0:
                pushHeap(c2)

        if maxHeap:
            ans += popHeap()
        return ans


