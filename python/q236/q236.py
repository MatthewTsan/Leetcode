class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def recurse(curr):
            if not curr:
                return False

            left = recurse(curr.left)
            right = recurse(curr.right)
            mid = curr == p or curr == q

            if left + right + mid >= 2:
                self.ans = curr

            return mid or left or right

        recurse(root)
        return self.ans

