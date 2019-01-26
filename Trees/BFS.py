from BST import BST
def bfs(root):

    if root is None:
        return

    queue = []

    queue.append(root)

    while len(queue) > 0:

        print(queue[0].val)
        node = queue.pop(0)

        if node.leftChild is not None:
            queue.append(node.leftChild)

        if node.rightChild is not None:
            queue.append(node.rightChild)





bst = BST(3)
bst.insert(5)
bst.insert(1)
bst.insert(6)
bst.insert(2)
bst.insert(0)
bst.insert(8)
bst.insert(10)
bst.insert(14)
bfs(bst.root)
