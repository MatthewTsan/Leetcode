# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(left, right):
            if left > right:
                return None
            val = postorder.pop()
            root = TreeNode(val)
            index = idx_map[val]
            root.right = build(index + 1, right)
            root.left = build(left, index - 1)
            return root

        idx_map = {val: index for index, val in enumerate(inorder)}
        return build(0, len(inorder) - 1)