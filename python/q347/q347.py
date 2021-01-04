class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict()
        for item in nums:
            hashMap[item] = hashMap.get(item, 0) + 1

        heap = []
        for key in hashMap:
            heapq.heappush(heap, (hashMap.get(key, 0), key))

        while len(heap) > k:
            heapq.heappop(heap)

        ans = [x[1] for x in heap]
        return ans