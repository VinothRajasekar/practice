def inorder(root):

    if root is none:
        return

    stack = []
    res = []

    while True:
        while root:
            stack.append(root)
            root = node.leftChild
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.rightChild
