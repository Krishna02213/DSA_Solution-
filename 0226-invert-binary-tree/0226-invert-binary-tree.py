class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Swap left and right child
        root.left, root.right = root.right, root.left

        # Invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root