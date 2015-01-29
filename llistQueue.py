#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter7: Queue Structure
#------------------------------------------
#Implements the Queue ADT using linked list

class Queue:
    #Create an empty Queue using list.
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    #Judge the Queue is empty or not according to self._size.
    def isEmpty(self):
        return self._size == 0

    #Return the number of items in Queue according to self._size.
    def __len__(self):
        return self._size

    #Add item in Queue tail using self._tail
    def enqueue(self,item):
        newNode = _QueueNode(item)
        print "newNode:",newNode._item
        if self._head == None:
            self._head = newNode
        else:
            self._tail.next = newNode
        self._tail = newNode
        print "tail:",self._tail._item
        self._size += 1

    #Return and remove the top item in the Queue after being sure the Queue is not empty.    
    def dequeue(self):
        assert not self.isEmpty(),"The Queue is empty"
        valueNode = self._head
        print "##self._head,",self._head._item
        if self._head is self._tail:
            self._tail = None
        self._head = valueNode._next
        self._size -= 1
        return valueNode._item

    #For debug:using overload operation __str__
    def __str__(self):
        print self._head._item
        print self._head._next._item
##        print "The elements in Queue is: ",
##        curNode = self._head
##        while curNode is not None:            
##            print curNode._item,
##            curNode = curNode._next
##            print "next:",curNode._item
##        return ""

class _QueueNode:
    def __init__(self,item):
        self._item = item
        self._next = None


#test
Q = Queue()
len(Q)
for i in range(10):
        Q.enqueue(i)
        #print "length of Q,",len(Q)
print "after enqueue:,",Q

