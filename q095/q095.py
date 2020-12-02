# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, nums):
        if len(nums) == 0:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[0])]

        res = []

        for i in range(len(nums)):
            l = self.buildTree(nums[:i])
            r = self.buildTree(nums[i + 1:])
            for ltree in l:
                for rtree in r:
                    root = TreeNode(nums[i])
                    root.left = ltree
                    root.right = rtree
                    res.append(root)
        return res

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        list = range(1, n + 1)
        return self.buildTree(list)

