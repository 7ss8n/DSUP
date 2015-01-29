#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter7: Stack Structures
#------------------------------------------
#Implements the Stack ADT using linked list
#using the tial of list as stack top and
#the head of list as stack base

class Stack:
    #Create an empty Stack using list.
    def __init__(self):
        self._top = None
        self._size = 0

    #Judge the Stack is empty or not.
    def isEmpty(self):
        return self._size == 0
        #also: return self._top is None

    #Return the number of items in Stack.
    def __len__(self):
        return self._size

    #Add item in Stack top.
    def push(self,item):
        newNode = _StackNode(item)
        newNode._next = self._top
        self._top = newNode
        self._size += 1

    #Return the top item in the Stack after being sure the stack is not empty.
    def peek(self):
        assert not self.isEmpty(),"The stack is empty"
        return self._top._item

    #Return and remove the top item in the Stack after being sure the stack is not empty.    
    def pop(self):
        assert not self.isEmpty(),"The stack is empty"
        value = self._top._item
        self._top = self._top._next
        self._size -= 1
        return value

    #For debug:using overload operation __str__
    def __str__(self):
        curNode = self._top
        print "The Stack is :",
        while curNode is not None:
            print curNode._item,
            curNode = curNode._next
        return ""
        
    
class _StackNode:
    def __init__(self,item):
        self._item = item
        self._next = None
