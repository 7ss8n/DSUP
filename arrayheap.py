#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter13: Binary Tree Structures
#------------------------------------------
#Implements the Heap ADT.

from array1 import Array

class MaxHeap:
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
        print "Heap: ",
        for i in range(self._count):
            print self._elements[i],
        return ""
        
    def _siftUp(self,n):
        index = n
        while index >0:
            parent = (index-1)/2
            child = index
            if self._elements[child] <= self._elements[parent]:
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
            maxChild = max(self._elements[left],self._elements[right])
            if self._elements[parent] >= maxChild:
                break
            else:
                if self._elements[left] >= self._elements[right]:
                    self._elements[parent],self._elements[left] = self._elements[left],self._elements[parent]
                    index = 2*index + 1
                else:
                    self._elements[parent],self._elements[right] = self._elements[right],self._elements[parent]
                    index = 2*index + 2
        

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
        print "Heap: ",
        for i in range(self._count):
            print self._elements[i],
        return ""
        
    def _siftUp(self,n):
        index = n
        while index >0:
            parent = (index-1)/2
            child = index
            if self._elements[child] >= self._elements[parent]:
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
            minChild = imn(self._elements[left],self._elements[right])
            if self._elements[parent] <= minChild:
                break
            else:
                if self._elements[left] <= self._elements[right]:
                    self._elements[parent],self._elements[left] = self._elements[left],self._elements[parent]
                    index = 2*index + 1
                else:
                    self._elements[parent],self._elements[right] = self._elements[right],self._elements[parent]
                    index = 2*index + 2

#testcase

def main():
    H = MaxHeap(16)
    H.add(100)
    H.add(84)
    H.add(71)
    H.add(60)
    H.add(23)
    H.add(12)
    H.add(29)
    H.add(1)
    H.add(37)
    H.add(4)
    H.add(90)
    H.add(41)
    print H
    print H.extract()
    print H

#main()


def simpleHeadpSort(theSeq):
    n = len(theSeq)
    H = MaxHeap(n)
    for elem in theSeq:
        H.add(elem)
    for i in range(n):
        theSeq[i] = H.extract()

lst = [1,3,2,4,5]
simpleHeadpSort(lst)
print lst


