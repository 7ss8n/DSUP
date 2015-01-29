#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter7: Stack Structures
#------------------------------------------
#Implements the Stack ADT using list
#using the tial of list as stack top and
#the head of list as stack base

class Stack:
    #Create an empty Stack using list.
    def __init__(self):
        self._stack = list()

    #Judge the Stack is empty or not according to the len of list.
    def isEmpty(self):
        return len(self._stack) == 0

    #Return the number of items in Stack according to the list length.
    def __len__(self):
        return len(self._stack)

    #Add item in Stack top using list method:append.
    def push(self,item):
        self._stack.append(item)

    #Return the top item in the Stack after being sure the stack is not empty.
    def peek(self):
        assert not self.isEmpty(),"The stack is empty"
        return self._stack[-1]

    #Return and remove the top item in the Stack after being sure the stack is not empty.    
    def pop(self):
        assert not self.isEmpty(),"The stack is empty"
        return self._stack.pop()

    #For debug:using overload operation __str__
    def __str__(self):
        for elem in self._stack:
            print elem,
        return ""
        
    
