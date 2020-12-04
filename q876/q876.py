# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        if fast.next:
            p = slow
            slow = slow.next
            p.next = None
        return slow