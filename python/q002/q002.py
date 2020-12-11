# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def Node2List(self, head):
        p = head
        list = [p.val]
        while p.next != None:
            p = p.next
            list.append(p.val)
        return list

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        head = ListNode((p1.val + p2.val) % 10)
        p = head
        tem = (p1.val + p2.val) // 10
        if p1.next == None and p2.next != None:
            p1.next = ListNode(0)
        if p2.next == None and p1.next != None:
            p2.next = ListNode(0)

        # num2Forms.print_ListNode(p1)
        # num2Forms.print_ListNode(p2)
        # num2Forms.print_ListNode(head)
        # print(tem)

        while p1.next != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next
            p.next = ListNode((p1.val + p2.val + tem) % 10)
            p = p.next
            tem = (p1.val + p2.val + tem) // 10
            # num2Forms.print_ListNode(p1)
            # num2Forms.print_ListNode(p2)
            # num2Forms.print_ListNode(head)
            # print(tem)
            if p1.next == None and p2.next != None:
                p1.next = ListNode(0)
            if p2.next == None and p1.next != None:
                p2.next = ListNode(0)

        # print(tem)
        if tem != 0:
            p.next = ListNode(tem)

        result = self.Node2List(head)
        return result


class num2Forms:
    @classmethod
    def num2ListNode(cls, num):
        head = ListNode(num % 10)
        p = head
        num = num // 10
        while num != 0:
            node = ListNode(num % 10)
            num = num // 10
            p.next = node
            p = node
        return head

    @classmethod
    def print_ListNode(cls, head):
        p = head
        print(p.val, end="")
        while p.next != None:
            p = p.next
            print(" -> ", p.val, end="")
        print("\n")

    @classmethod
    def num2List(cls, num):
        if num == 0:
            return [0]
        list = []
        while num != 0:
            list.append(num % 10)
            num = num // 10
        return list
