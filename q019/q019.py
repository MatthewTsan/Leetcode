# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0 or not head:
            return head
        # walk N step, p = head. if None, then return,
        cur = head
        while n > 0 and cur:
            cur = cur.next
            n -= 1
        if not cur:
            if n == 0:
                return head.next
            return head

        # walk until None, delete p
        p = head
        prep = head
        if not cur.next:
            head.next = head.next.next
            return head
        while cur:
            cur, prep, p = cur.next, p, p.next
        prep.next = prep.next.next

        return head
