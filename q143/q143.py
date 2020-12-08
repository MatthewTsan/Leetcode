# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Split the list
        slow = fast = head
        preslow = slow
        while fast and fast.next:
            preslow = slow
            slow, fast = slow.next, fast.next.next
        if fast:
            preslow = slow
            slow = slow.next
        preslow.next = None
        head2 = slow
        if not head2:
            return

        # reverse the head2
        pre, cur = head2, head2.next
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        head2.next = None
        head2 = pre

        # # merge two linklist
        p = head
        while p and head2:
            node = head2
            p.next, node.next, head2, p = node, p.next, head2.next, p.next