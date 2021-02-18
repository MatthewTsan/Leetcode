# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = []
        # BFS
        queue = deque()
        queue.append([root, 0])
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])

            if not queue:
                ans.append(node.val)
            elif queue[0][1] > depth:
                ans.append(node.val)

        return ans
