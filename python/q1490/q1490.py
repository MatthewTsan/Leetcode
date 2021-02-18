# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []



class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def build(node):
            if node is None:
                return None
            p = Node(node.val)
            for child in node.children:
                p.children.append(build(child))
            return p

        return build(root)