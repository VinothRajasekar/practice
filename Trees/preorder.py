def preorder(root):

    if root is None:
        return []

    res =[]
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.leftChild)
            stack.append(node.rightChild)
    return res
