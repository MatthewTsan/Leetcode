# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.__nodeList = list()
        self.__index = -1
        self.__inorder(root)

    def __inorder(self, root):
        if root is None:
            return
        self.__inorder(root.left)
        self.__nodeList.append(root.val)
        self.__inorder(root.right)

    def next(self) -> int:
        self.__index += 1
        return self.__nodeList[self.__index]

    def hasNext(self) -> bool:
        return self.__index < len(self.__nodeList) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
