# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def __init__(self):
        self.result = []


    def __recursiveTraversal(self, root: TreeNode):
        if root is None:
            return
        self.result.append(root.val)
        self.__recursiveTraversal(root.left)
        self.__recursiveTraversal(root.right)

    def __loopTraversal(self, root: TreeNode):
        if root is None:
            return
        stack = []
        stack.append(root)
        while stack:
            print(stack)
            if stack[-1] is None:
                del stack[-1]
                continue
            top = stack[-1]
            del stack[-1]
            self.result.append(top.val)

            stack.append(top.right)
            stack.append(top.left)


    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # self.__recursiveTraversal(root)
        self.__loopTraversal(root)
        return self.result

def addNode(root, data):
    if data > root.val:
        if root.right:
            addNode(root.right, data)
        else:
            root.right = TreeNode(data)
    else:
        if root.left:
            addNode(root.left, data)
        else:
            root.left = TreeNode(data)

if __name__ == '__main__':
    list = [1, 4, 3, 5, 2]
    root = TreeNode(list[0])
    for item in list[1:]:
        addNode(root, item)
    sol = Solution()
    sol.preorderTraversal(root)
    print(sol.result)