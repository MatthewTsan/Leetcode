# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root, 0])
        ans = []
        level = []
        while queue:
            top, depth = queue.popleft()
            if top.left:
                queue.append([top.left, depth+1])
            if top.right:
                queue.append([top.right, depth+1])
            level.append(top.val)
            if queue and depth < queue[0][1]:
                ans.append(level)
                level = []
        ans.append(level)
        return ans