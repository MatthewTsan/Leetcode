# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dictP = {}
        newHead = Node(0)
        p_ori = head
        p_new = newHead

        id = 0
        while p_ori:
            p_new.next = Node(p_ori.val)
            dictP[p_ori] = p_new.next

            p_new, p_ori = p_new.next, p_ori.next

        p_ori = head
        p_new = newHead.next
        while p_ori:
            if p_ori.random != None:
                p_new.random = dictP[p_ori.random]

            p_new, p_ori = p_new.next, p_ori.next

        return newHead.next
