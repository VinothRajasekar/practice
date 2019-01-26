from TreeNode import Node

class BST:

    def __init__(self,val):

        self.root = Node(val)

    def setRoot(self,val):
        self.root = Node(val)

    def getRoot(self):
        return self.root.get()

    def insert(self,val):
        self.root.insert(val)

    def search(self,val):
        return self.root.search(val)

def inorder(node):
    if node!=None:
       inorder(node.leftChild)
       print(node.val)
       inorder(node.rightChild)

def preorder(node):
    if node!=None:
        print(node.val)
        preorder(node.leftChild)
        preorder(node.rightChild)

def postorder(node):
    if node!=None:
        postorder(node.leftChild)
        postorder(node.rightChild)
        print(node.val)






# bst = BST(3)
# bst.insert(5)
# bst.insert(1)
# bst.insert(6)
# bst.insert(2)
# bst.insert(0)
# bst.insert(8)
# bst.insert(10)
# bst.insert(14)

#print(str(bst.getRoot()))
#preorder(bst.root)
# print(bst.search(122))
