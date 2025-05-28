from collections import deque

class Solution:
    def isParent(self, root: Optional[TreeNode], a: int, b: int) -> bool:
        if root is None:
            return False
        
        if root.left and root.right:
            if (root.left.val == a and root.right.val == b) or \
               (root.left.val == b and root.right.val == a):
                return True
        
        return self.isParent(root.left, a, b) or self.isParent(root.right, a, b)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue = deque([root])
        level = 0
        l1 = l2 = -1

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.val == x:
                    l1 = level
                if node.val == y:
                    l2 = level
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

            if l1 != -1 and l2 != -1:
                break
            if l1 != l2:  # One found but not the other
                return False

        if l1 == -1 or l2 == -1:
            return False  # One or both not found

        return not self.isParent(root, x, y)
