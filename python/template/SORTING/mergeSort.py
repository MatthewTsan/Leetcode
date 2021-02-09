# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def split(self, head: ListNode) -> (ListNode, ListNode):
        # print("split: ")
        # self.printListNode(head)

        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
        p = slow
        slow = slow.next
        p.next = None
        return head, slow

    def merge(self, p1, p2):
        # print("\n\nmerge")
        # self.printListNode(p1)
        # self.printListNode(p2)

        head = ListNode()
        p = head
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
                p.next = None
            else:
                p.next = p2
                p = p.next
                p2 = p2.next
                p.next = None
            # print("temResult")
            # self.printListNode(head)
            # print("p1")
            # self.printListNode(p1)
            # print("p2")
            # self.printListNode(p2)
            # print("\n")
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        # print("merge result:")
        # self.printListNode(head)
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        # print("\n\nsortList:")
        # self.printListNode(head)

        if not head:
            return head

        head, mid = self.split(head)
        if not head or not mid:
            return head
        head = self.sortList(head)
        mid = self.sortList(mid)
        head = self.merge(head, mid)
        # self.printListNode(head)
        return head


    def printListNode(self, head):
        print("Link List: ")
        while head:
            print(head.val, end=" ")
            head = head.next
        print()



if __name__ == '__main__':
    list = [2, 4, 1, 3]
    head = p = ListNode()
    for item in list:
        p.next = ListNode(item)
        p = p.next
    head = head.next
    solution = Solution()

    head = solution.sortList(head)
    solution.printListNode(head)

    # head, mid = solution.split(head)
    # head = solution.merge(head, mid)
    # solution.printListNode(head)
