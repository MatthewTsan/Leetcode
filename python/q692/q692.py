from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = defaultdict()
        for s in words:
            hashMap[s] = hashMap.get(s, 0) + 1

        heap = []
        for key in hashMap:
            heapq.heappush(heap, (-hashMap.get(key, 0), key))

        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans[:k]