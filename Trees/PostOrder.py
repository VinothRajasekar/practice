def postorder(root):

    if root is None:
        return None

    stack, res = [root,], []

    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.leftChild is None:
            res.append(root.leftChild)
        if root.rightChild is None:
            res.append(root.rightChild)
    return output[::-1]
