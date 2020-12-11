# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def heapify(self, heap, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        # print(i, n, left, right, heap)
        if left < n and heap[i].val > heap[left].val:
            smallest = left
        if right < n and heap[smallest].val > heap[right].val:
            smallest = right
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(heap, smallest, n)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = p = ListNode()
        minHeap = []
        for l in lists:
            if l:
                minHeap.append(l)
        count = len(minHeap)

        # construct the heap:
        for i in range(count // 2 - 1, -1, -1):
            self.heapify(minHeap, i, count)

        while count:
            p.next = minHeap[0]
            p = p.next

            l = minHeap[0].next
            if l:
                minHeap[0] = l
                self.heapify(minHeap, 0, count)
            else:
                count -= 1
                minHeap[0], minHeap[count] = minHeap[count], minHeap[0]
                self.heapify(minHeap, 0, count)

        return head.next












