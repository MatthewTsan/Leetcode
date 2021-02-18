# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def DFS(node):
            if not node:
                return 0
            leftSum = max(DFS(node.left), 0)
            rightSum = max(DFS(node.right), 0)
            self.maxSum = max(self.maxSum, leftSum + rightSum + node.val)
            return node.val + max(leftSum, rightSum)

        self.maxSum = -math.inf
        DFS(root)
        return self.maxSum
