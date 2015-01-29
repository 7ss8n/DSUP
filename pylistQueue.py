#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter8: Queue Structure
#------------------------------------------
#Implements the Queue ADT using Python list
#using the tial of list as Queue back
#the head of list as Queue front

class Queue:
    #Create an empty Queue using list.
    def __init__(self):
        self._theElements = list()

    #Judge the Queue is empty or not according to the len of list.
    def isEmpty(self):
        return len(self._theElements) == 0

    #Return the number of items in Queue according to the list length.
    def __len__(self):
        return len(self._theElements)

    #Add item in Queue top using list method:append.
    def enqueue(self,item):
        self._theElements.append(item)

    #Return and remove the top item in the Queue after being sure the Queue is not empty.    
    def dequeue(self):
        assert not self.isEmpty(),"The Queue is empty"
        return self._theElements.pop(0)

    #For debug:using overload operation __str__
    def __str__(self):
        print "The elements in Queue is: ",
        for elem in self._theElements:
            print elem,
        return ""

"""        
#test
Q = Queue()
len(Q)
0
for i in range(30):
    if i%3 == 0:
            Q.enqueue(i)
            print "after enqueue:,",Q
    elif i%4 == 0:
            Q.dequeue()
            print "after Dequeue:,",Q    
""" 
