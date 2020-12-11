# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __build(self, preorder:List[int], rootIndex, inorder:List[int], bg, ed) -> TreeNode:
        if bg == ed:
            return None

        if rootIndex == len(preorder) - 1:
            return None

        root = TreeNode(preorder[rootIndex])
        print(root.val, bg, ed)
        inorderIndex = inorder.index(root.val)
        print("into left:", preorder[rootIndex+1], bg, inorderIndex)
        root.left = self.__build(preorder, rootIndex+1, inorder, bg, inorderIndex)

        print("into right:", preorder[rootIndex + inorderIndex - bg + 1], inorderIndex+1, ed)
        root.right = self.__build(preorder, rootIndex + + inorderIndex - bg + 1, inorder, inorderIndex+1, ed)
        print("\n\n")
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = self.__build(preorder, 0, inorder, 0, len(inorder))
        return root

def printTree(root: TreeNode):
    if root == None:
        return
    print(root.val, "(", printTree(root.left), ",", printTree(root.right), ")", end="")

sol = Solution()
preorder = [3, 9, 20, 4, 6, 7]
inorder = [20, 9, 3, 6, 4, 7]
root = sol.buildTree(preorder, inorder)
printTree(root)