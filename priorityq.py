#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter8: Queue Structure
#------------------------------------------
#Implements the PriorityQueue ADT using Python list
#using the tial of list as Queue back
#the head of list as Queue front

class PriorityQueue:
    #Create an empty unbounded Priority Queue queue
    def __init__(self):
        self._theElements = list()

    #Judge the Queue is empty or not according to the len of list.
    def isEmpty(self):
        return len(self._theElements) == 0

    #Return the number of items in Queue according to the list length.
    def __len__(self):
        return len(self._theElements)

    #Add item in Queue top using list method:append.
    def enqueue(self,item,priority):
        entry = _PriorityElem(item,priority)
        self._theElements.append(entry)

    #Return and remove the top item in the Queue after being sure the Queue is not empty.    
    def dequeue(self):
        assert not self.isEmpty(),"The Queue is empty."
        highest = 0
        for i in range(len(self._theElements)):
            if self._theElements[i]._priority < self._theElements[highest]._priority:
                highest = i
        entry = self._theElements.pop(highest)
        return entry._item

    #For debug:using overload operation __str__
    def __str__(self):
        print "The elements in Queue is: ",
        for elem in self._theElements:
            print elem,
        return ""

class _PriorityElem:
    def __init__(self,item,priority):
        self._item = item
        self._priority = priority


#test
Q = PriorityQueue()
Q.enqueue( "purple", 5 )
Q.enqueue( "black", 1 )
Q.enqueue( "orange", 3 )
Q.enqueue( "white", 0 )
Q.enqueue( "green", 1 )
Q.enqueue( "yellow", 5 )
print"Length of Q:",len(Q)
print Q.dequeue()
print Q.dequeue()
print Q.dequeue()
print Q.dequeue()
print Q.dequeue()
print Q.dequeue()
print Q.dequeue()

