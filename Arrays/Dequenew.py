class Deque:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        return self.items.append(item)

    def addRear(self,item):
        return self.items.insert(0,item)

    def removeFront(self,item):
        return self.items.pop()

    def removeRear(self,item):
        return self.items.pop(0)

    def printItems(self):
        return self.items


data = Deque()
print (data.isEmpty())
data.addFront(1)
print(data.printItems())
data.addRear(2)
print(data.printItems())
data.addFront(3)
print(data.printItems())
