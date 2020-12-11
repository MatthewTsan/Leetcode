# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        i = 1
        p = head
        pm = None
        while i < m:
            pm = p
            p = p.next
            i += 1
        if not p:
            return

        rList = ListNode(p.val)
        pr_end = rList
        p = p.next
        i += 1
        while i <= n:
            rList = ListNode(p.val, rList)
            p = p.next
            i += 1
        pn = p

        if pm == None:
            head = rList
        else:
            pm.next = rList
        pr_end.next = pn
        return head


