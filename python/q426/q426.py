
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = Node(0)
        self.last = self.head

        def inorder(root):
            if not root:
                return
            inorder(root.left)

            p = Node(root.val)
            self.last.right = p
            p.left = self.last

            self.last = self.last.right

            inorder(root.right)

        if not root:
            return None
        inorder(root)
        self.head = self.head.right
        self.last.right = self.head
        self.head.left = self.last
        return self.head