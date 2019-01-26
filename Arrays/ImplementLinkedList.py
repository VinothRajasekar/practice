class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def setData(self, newData):
        self.data = newData

    def getData(self):
        return self.data

    def setNext(self,newNext):
        self.next = newNext

    def getNext(self):
        return self.next

#temp = Node(10)
#print(temp.getData())

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty():
        return self.head == None

    def getHead(self):
        return self.head

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current!= None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False

        while current!=None and not found:
            if current.getData() == item:
                found = True
                print("item found in the list:" + str(item))
            else:
                current = current.getNext()

        return found

    def removeItem(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getData() == item:
               found = True
            else:
               previous = current
               current = current.getNext()

        if previous == None:
           self.head = current.getNext()
        else:
           previous.setNext(current.getNext())

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(35))
mylist.removeItem(31)
print(mylist.size())
