# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        p = head
        while(p.next != None):
            self.printLinkList(p)
            NodeToBeMoved = p.next
            p.next = NodeToBeMoved.next
            temp = head
            if(NodeToBeMoved.val < temp.val):
                NodeToBeMoved.next = temp
                head = NodeToBeMoved
            else:
                while(temp.next != None and NodeToBeMoved.val > temp.next.val):
                    temp = temp.next
                tempNext = temp.next
                temp.next = NodeToBeMoved
                NodeToBeMoved.next = tempNext
            p = p.next

    @staticmethod
    def printLinkList(head: ListNode):
        p = head
        print('print')
        while (p != None):
            print(p.val, end=" ")
            p = p.next 
        print()

sol = Solution()
list = [4, 2, 1, 3]
head = ListNode(list[0])
p = head
for item in list[1:]:
    p.next = ListNode(item)
Solution.printLinkList(head)
sol.insertionSortList(head)
sol.printLinkList(head)