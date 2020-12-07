# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def split(self, head):
        slow = head
        fast = head
        slow_pre = head
        while fast and fast.next:
            slow_pre = slow
            slow, fast = slow.next, fast.next.next

        slow_pre.next = None
        return head, slow

    def merge(self, p1, p2):
        if not p2:
            return p1
        if not p1:
            return p2

        head = ListNode()
        p = head
        while p1 and p2:
            if p1.val < p2.val:
                p.next = ListNode(p1.val)
                p = p.next
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p = p.next
                p2 = p2.next

        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return head.next

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        p1, p2 = self.split(head)
        p1 = self.mergeSort(p1)
        p2 = self.mergeSort(p2)
        head = self.merge(p1, p2)
        return head

    def sortList(self, head: ListNode) -> ListNode:
        return self.mergeSort(head)


