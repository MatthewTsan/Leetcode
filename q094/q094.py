# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = []

    def __inorderTraversal_recursive(self, root: TreeNode):
        if root == None:
            return

        if root.left != None:
            self.__inorderTraversal_recursive(root.left)

        self.ans.append(root.val)

        if root.right != None:
            self.__inorderTraversal_recursive(root.right)

    def __inorderTraversal_iterative(self, root: TreeNode):
        if root == None:
            return
        #
        # stack = []
        # current = root
        # while(current != None and stack):
        #     while current != None:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop(-1)
        #     self.ans.append(current.val)
        #     current = current.right

        stack = [root]
        current: TreeNode = root
        while stack:
            # for item in stack:
            #     print(item.val, end=" ")
            # print()

            while current.left != None:
                stack.append(current.left)
                current = current.left
            current = stack.pop(-1)
            # print("current", current.val)
            self.ans.append(current.val)
            if current.right != None:
                stack.append(current.right)
                current = current.right

            # print("\n\n")

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.__init__()
        self.__inorderTraversal_iterative(root)

        return self.ans

sol = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
sol.inorderTraversal(root)
print(sol.ans)