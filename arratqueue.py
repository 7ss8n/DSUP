#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter8: Queue Structure
#------------------------------------------
#Implements the Queue ADT using circular array
#which has a max capicity
from array1 import Array

class Queue:
    #Create an empty Queue using list.
    def __init__(self,maxSize):
        self._theElements = Array(maxSize)
        self._head = 0
        self._back = (maxSize-1)
        self._count = 0

    #Judge the Queue is empty or not according to self._count.
    def isEmpty(self):
        return self._count == 0
    
    #Judge the Queue is empty or not according to self._count.
    def isFull(self):
        return self._count == len(self._theElements)

    #Return the number of items in Queue according to self._count.
    def __len__(self):
        return self._count

    #Add item in Queue tail.
    def enqueue(self,item):
        assert not self.isFull(),"The Queue is full!"
        maxSize = len(self._theElements)
        self._back  = (self._back + 1) % maxSize
        self._theElements[self._back] = item
        self._count += 1
        

    #Return and remove the top item in the Queue after being sure the Queue is not empty.    
    def dequeue(self):
        assert not self.isEmpty(),"The Queue is empty"
        maxSize = len(self._theElements)
        item = self._theElements[self._head]
        self._head  = (self._head + 1) % maxSize
        self._count -= 1
        return item

    #For debug:using overload operation __str__
    def __str__(self):
        maxSize = len(self._theElements)
        if  self._count == 0:
            print "",
        elif self._head == self._back:
            print self._theElements[self._head],
        elif self._head < self._back:
            for i in range(self._head,self._back+1):
                print self._theElements[i],
        elif self._head > self._back:
            for i in range(self._head,maxSize+1):
                print self._theElements[i],
            for i in range(0,self._head+1):
                print self._theElements[i] ,          
        return ""

       
#test
Q = Queue(15)
print "length,",len(Q)
for i in range(30):
    if i%3 == 0:
            Q.enqueue(i)
            print "after enqueue:,",Q           
    elif i%5 == 0:
            Q.dequeue()
            print "after Dequeue:,",Q    

