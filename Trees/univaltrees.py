from BST import BST

def univaltrees(node,count):

    if node is None:
        return True

    left = univaltrees(node.leftChild,count)
    right = univaltrees(node.rightChild,count)

    if left == False or right == False:
        return False

    if node.leftChild and node.val != node.leftChild.val:
        return False


    if node.rightChild and node.val != node.rightChild.val:
        return False

    count[0] +=1
    print(count)
    return True


bst = BST(5)
bst.insert(4)
bst.insert(5)
bst.insert(4)
bst.insert(4)
bst.insert(5)
count=[0]
univaltrees(bst.root,count)
