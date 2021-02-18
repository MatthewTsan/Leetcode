# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        left = []
        if root.left:
            node = root.left
            while node.left or node.right:
                left.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        right = []
        if root.right:
            node = root.right
            while node.left or node.right:
                right.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        right.reverse()

        leaf = []
        if root.left or root.right:
            def DFS(leaf, node):
                if not node:
                    return
                if node.left or node.right:
                    DFS(leaf, node.left)
                    DFS(leaf, node.right)
                else:
                    leaf.append(node.val)

            DFS(leaf, root)

        # print(left)
        # print(leaf)
        # print(right)
        return [root.val] + left + leaf + right