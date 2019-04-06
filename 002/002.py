# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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

        while p1.next != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next
            p.next = ListNode((p1.val + p2.val + tem) % 10)
            p = p.next
            tem = (p1.val + p2.val) // 10
            if p1.next == None and p2.next != None:
                p1.next = ListNode(0)
            if p2.next == None and p1.next != None:
                p2.next = ListNode(0)

        if tem != 0:
            p.next = ListNode(tem)

        return head

class num2ListNode:
    def num2ListNode(self, num):
        head = ListNode(num % 10)
        p = head
        num = num // 10
        while num != 0:
            node = ListNode(num % 10)
            num = num // 10
            p.next = node
            p = node
        return head

    def print_ListNode(self, head):
        p = head
        print(p.val, end="")
        while p.next != None:
            p = p.next
            print(" -> ", p.val, end="")


if __name__ == '__main__':
    number1 = num2ListNode().num2ListNode(243)
    number2 = num2ListNode().num2ListNode(564)
    result = Solution().addTwoNumbers(number1, number2)
    num2ListNode().print_ListNode(result)