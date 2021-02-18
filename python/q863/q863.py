# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parMap = defaultdict(TreeNode)

        def DFS(node, par):
            if node is None:
                return
            parMap[node] = par
            DFS(node.left, node)
            DFS(node.right, node)

        DFS(root, None)

        queue = deque()
        queue.append([target, 0])
        visit = []
        visit.append(target)
        while queue:
            # print([node.val for node, _ in queue])
            if queue[0][1] == K:
                return [node.val for node, _ in queue]
            node, distence = queue.popleft()
            for neibor in (node.left, node.right, parMap[node]):
                if neibor and neibor not in visit:
                    visit.append(neibor)
                    queue.append([neibor, distence + 1])
        return []