# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.ans = []

        def DFS(root, depth):
            if not root:
                return
            if len(self.ans) < depth + 1:
                self.ans.append([root.val])
            else:
                self.ans[depth].append(root.val)
            DFS(root.left, depth + 1)
            DFS(root.right, depth + 1)

        DFS(root, 0)
        self.ans.reverse()
        return self.ans