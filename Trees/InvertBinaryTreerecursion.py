    def invertTree(self, root):
        if root is None:
            return None
        root.left=self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        return root
