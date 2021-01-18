class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            maxVal = max(p.val, q.val)
            minVal = min(p.val, q.val)
            if node.val > maxVal:
                node = node.left
            elif node.val < minVal:
                node = node.right
            else:
                return node

        return None