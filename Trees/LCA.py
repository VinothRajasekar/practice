from BST import BST

def lca(root, a, b):

    if root.val == a or root.val == b:
        return root

    left = right = None

    if root.leftChild:
       left = lca(root.leftChild, a, b)

    if root.rightChild:
       right = lca(root.rightChild, a, b)

    if left and right:
        return root
    else:
        return left or right

def inorder(node):
    if node!=None:
       print(node.val)
       inorder(node.leftChild)
       inorder(node.rightChild)

bst = BST(3)
bst.insert(5)
bst.insert(1)
bst.insert(6)
bst.insert(2)
bst.insert(0)
bst.insert(8)
bst.insert(10)
bst.insert(14)
#print(bst.root.val)
l = lca(bst.root,2,0)
print(l.val)
#print(inorder(bst.root))
