# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def check(original, target):
            if original is None or target is None:
                if original is None and target is None:
                    return True
                else:
                    return False
            return original.val == target.val and check(original.left, target.left) and check(original.right,
                                                                                              target.right)

        def DFS(original, target):
            if original is None or target is None:
                if original is None and target is None:
                    return True
                else:
                    return False
            if original.val == target.val and check(original, target):
                return True
            else:
                return DFS(original.left, target) or DFS(original.right, target)

        return DFS(s, t)
