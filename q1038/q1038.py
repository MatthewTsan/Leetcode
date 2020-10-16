# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def DFS(self, root: TreeNode, sum):
        if root:
            right = self.DFS(root.right, sum)
            root.val += right
            left = self.DFS(root.left, root.val)
            return left
        return sum

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.DFS(root, 0)
        return root


def add(node, data):
    if data > node.val:
        if node.right:
            add(node.right, data)
            return
        else:
            node.right = TreeNode(data)
            return
    else:
        if node.left:
            add(node.left, data)
            return
        else:
            node.left = TreeNode(data)
            return


def printTree(root: TreeNode):
    list = []
    result = []
    list.append(root)
    while list:
        print(list)
        if list[0] is None:
            result.append(None)
            del list[0]
            continue
        result.append(list[0].val)
        list.append(list[0].left)
        list.append(list[0].right)
        del list[0]
    print(result)


if __name__ == '__main__':
    list = [4, 1, 6, 0, 2, 5, 7, 3, 8]
    root = TreeNode(list[0])
    for item in list[1:]:
        add(root, item)
    printTree(root)

    sol = Solution()
    sol.bstToGst(root)
    printTree(root)

