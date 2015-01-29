#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter13: Binary Tree Structures
#------------------------------------------
#Implements the Priority Queue ADT using Min HeapADT

##from arrayheap import MinHeap
from array1 import Array

class PriorityQueue:
    #Create an empty unbounded Priority Queue queue
    def __init__(self,maxSize):
        self._theElements = MinHeap(maxSize)
        self._capacity = maxSize
        

    #Judge the Queue is empty.
    def isEmpty(self):
        return len(self._theElements) == 0

    #Judge the Queue is empty.
    def isFull(self):
        return len(self._theElements) == self._capacity

    #Return the number of items in Queue.
    def __len__(self):
        return len(self._theElements)    

    #Add item in Queue top using list method:append.
    def enqueue(self,item,priority):
        assert not self.isFull(),"The Queue is Full."
        entry = _PriorityElem(item,priority)
        self._theElements.add(entry)

    #Return and remove the top item in the Queue after being sure the Queue is not empty.    
    def dequeue(self):
        assert not self.isEmpty(),"The Queue is empty."
        entry = self._theElements.extract()
        return entry

    #For debug:using overload operation __str__
    def __str__(self):
        print "The Queue is: "
        print self._theElements
        return ""
        


class _PriorityElem:
    def __init__(self,item,priority):
        self.item = item
        self.key = priority


class MinHeap:
    def __init__(self,maxSize):
        self._elements = Array(maxSize)
        self._count = 0

    def __len__(self):
        return self._count

    def capacity(self):
        return len(self._elements)

    def add(self,value):
        assert self._count < self.capacity,"Cannot add to a full heap."
        #Add the value to the end of the Array.
        self._elements[self._count] = value
        self._count += 1
        self._siftUp(self._count-1)

    def extract(self):
        assert self._count > 0,"Cannot remove from a empty heap."
        #remove the top(max) element of the Array.
        #print "Before extract:count = ",self._count 
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftDown(0)
        #print "After extract:count = ",self._count
        return value


    def __str__(self):
        #print "Heap: ",
        for i in range(self._count):
            print """({0}),'{1}'""".format(self._elements[i].key,self._elements[i].item)
        return ""
        
    def _siftUp(self,n):
        index = n
        while index >0:
            parent = (index-1)/2
            child = index
            if self._elements[child].key >= self._elements[parent].key:
                break
            else:
                self._elements[child],self._elements[parent] = self._elements[parent],self._elements[child]
                index = (index-1)/2
        

    def _siftDown(self,n):
        index = n
        while 2*index +2 <= self._count:
            #print "index = ",index
            parent = index
            left = 2*index + 1
            right = 2*index + 2
            minChild = imn(self._elements[left].key,self._elements[right].key)
            if self._elements[parent].key <= minChild.key:
                break
            else:
                if self._elements[left].key <= self._elements[right].key:
                    self._elements[parent],self._elements[left] = self._elements[left],self._elements[parent]
                    index = 2*index + 1
                else:
                    self._elements[parent],self._elements[right] = self._elements[right],self._elements[parent]
                    index = 2*index + 2

                    
