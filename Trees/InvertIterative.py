def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop(-1)
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root
