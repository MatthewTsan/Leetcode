# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            top = queue.popleft()
            if top != None:
                ans.append(str(top.val))
                queue.append(top.left)
                queue.append(top.right)
            else:
                ans.append(str("null"))
        while ans[-1] == "null":
            ans.pop()

        return "\n".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        nodeQ = deque(data.split("\n"))
        queue = deque()

        head = TreeNode(int(nodeQ.popleft()))
        queue.append(head)
        while queue:
            # print([node.val for node in queue])
            # print(nodeQ)
            top = queue.popleft()
            left = "null" if not nodeQ else nodeQ.popleft()
            right = "null" if not nodeQ else nodeQ.popleft()
            top.left = None if left == "null" else TreeNode(int(left))
            top.right = None if right == "null" else TreeNode(int(right))
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return head

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))