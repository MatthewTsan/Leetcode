# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.map = defaultdict(Node)

        def build(node):
            if node is None:
                return None
            if node in self.map:
                return self.map[node]
            p = Node(node.val)
            self.map[node] = p
            for nei in node.neighbors:
                p.neighbors.append(build(nei))
            return p

        return build(node)
