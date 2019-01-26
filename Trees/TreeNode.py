class Node:

    def __init__(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self,val):
        self.val = val

    def insert(self, val):

        if self is None:
            self = Node(val)
            return
        if val < self.val:
            print("head", self.val)
            if self.leftChild:
                self.leftChild.insert(val)
            else:
                self.leftChild = Node(val)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(val)
            else:
                self.rightChild = Node(val)
                return

    def search(self,val):

        if self is None or self.val == val:
            return self
        elif val < self.val:
            if self.leftChild:
                return self.leftChild.search(val)
            else:
                return None
        else:
            if self.rightChild:
                return self.rightChild.search(val)
            else:
                return None
