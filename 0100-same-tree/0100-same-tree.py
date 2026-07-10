class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both null -> same
        if not p and not q:
            return True
        
        # One null, one not -> different
        if not p or not q:
            return False
        
        # Values differ -> different
        if p.val != q.val:
            return False
        
        # Recursively check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)