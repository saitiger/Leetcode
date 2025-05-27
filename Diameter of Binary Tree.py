class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node:
                return 0
            left = solve(node.left)
            right = solve(node.right)
            self.res = max(self.res, left + right)  # Update diameter
            return 1 + max(left, right)  # Return height

        self.res = 0
        solve(root)
        return self.res
