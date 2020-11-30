# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []


    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # self.__recursiveTraversal(root)
        self.__loopTraversal(root)
        return self.result

    def __recursiveTraversal(self, root):
        if root is None:
            return
        self.__recursiveTraversal(root.left)
        self.__recursiveTraversal(root.right)
        self.result.append(root.val)

    def __loopTraversal(self, root):
        # stack = [root]
        # prev = None
        # for i in range(2):
        #     print(list(map(lambda x: x.val, stack)))
        #     while stack[-1].left:
        #         stack.append(stack.left)
        #     if stack:
        #         p = stack.pop(-1)
        #         print(prev, p.right, prev == p.right)
        #         if p.right is None or prev == p.right:
        #             self.result.append(p.val)  # access the Node
        #             prev = p
        #             p = p.null
        #         else:
        #             stack.append(p)
        #             p = p.right
        #     print(list(map(lambda x: x.val, stack)), end="\n\n\n")
        stack = []
        stack.append(root)
        while stack:
            while(stack[-1].left):
                stack.append(stack[-1].left)

            p = stack.pop


def addNode(root, val):
    if val > root.val:
        if root.right:
            addNode(root.right, val)
        else:
            root.right = TreeNode(val)
    else:
        if root.left:
            addNode(root.left, val)
        else:
            root.left = TreeNode(val)


if __name__ == '__main__':
    data = [1, 4, 3, 2, 5]
    root = TreeNode(data[0])
    for item in data[1:]:
        addNode(root, item)

    sol = Solution()
    res = sol.postorderTraversal(root)
    print(res)
