class maxHeap:

    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.__perlocateUp(len(self.heap)-1)

    def getMax(self):

        if self.heap:
           return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1 :
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    def __perlocateUp(self,index):
        parent = index //2
        print(parent, index)
        if index <=0:
            print("here")
            return
        elif self.heap[parent] < self.heap[index]:
             tmp = self.heap[parent]
             self.heap[parent] = self.heap[index]
             self.heap[index]= tmp
             self.__perlocateUp(parent)

    def __maxHeapify(self, index):
        print("barro" + str(index))
        left = index * 2
        right = (index * 2) + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest!=index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__maxHeapify(largest)



heap = maxHeap();
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
heap.removeMax()
print(heap.getMax())
