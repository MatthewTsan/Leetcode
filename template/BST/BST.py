class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


"""
template for Binary search tree.

Note:
    there is no duplicate data in the tree.
"""


class BST:
    def __init__(self):
        self.__root = None

    def find(self, data: TreeNode):
        result = self.__root
        while result is not None and result.val != data:
            if result.val < data:
                result = result.right
            else:
                result = result.left
        return result

    def add(self, data):
        if self.__root is None:
            self.__root = TreeNode(data)
            return
        else:
            pos = self.__root
            father = None
            while pos is not None:
                father = pos
                if pos.val < data:
                    pos = pos.right
                else:
                    pos = pos.left
            print(father.val)
            print(pos)
            pos = TreeNode(data)
            if father.val < data:
                father.right = pos
            else:
                father.left = pos

    def delete(self, data):
        pos = self.find(data)
        if pos is None:
            return
        if pos == self.__root:
            if self.__root.right is None:
                self.__root = self.__root.left
                return
            else:
                p = pos.right
                pFather = pos
                while p.left is not None:
                    pFather = p
                    p = p.left
                pFather.left = None
                self.__root.val = p.val
                return

        posFather = self.__root
        if data > self.__root.val:
            pos = self.__root.right
        else:
            pos = self.__root.left
        while pos.val != data:
            posFather = pos
            if data > pos.val:
                pos = pos.right
            else:
                pos = pos.left
        if pos.right is None:
            if pos == posFather.left:
                posFather.left = pos.left
            else:
                posFather.right = pos.left
        else:
            # print(posFather.data, pos.data)
            pFather = pos
            p = pos.right
            if p.left is None:
                pos.val = p.val
                pos.right = None
            else:
                while p.left is not None:
                    pFather = p
                    p = p.left
                # print(pFather.data, p.data)
                pos.val = p.val
                pFather.left = None

    def __printRecursive(self, node):
        if node is None:
            return

        print(node.data, "(", end="")
        self.__printRecursive(node.left)
        print(", ", end=" ")
        self.__printRecursive(node.right)
        print(")", end="")

    def printTree(self):
        self.__printRecursive(self.__root)
        print()

    def getRoot(self):
        return self.__root


if __name__ == '__main__':
    list = [1, 6, 5, 4, 10, 9, 8, 7]
    tree = BST()
    for item in list:
        print("add", item)
        tree.add(item)
        tree.printTree()

    tree.printTree()

    print(tree.find(6))
    print(tree.find(4).val)

    tree.delete(6)
    tree.printTree()