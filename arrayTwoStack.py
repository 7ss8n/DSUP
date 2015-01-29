#http://www.geeksforgeeks.org/implement-two-stacks-in-an-array/
#Impelment two stack using an array
#Following fucntions must be supported by twoStacks
#push1(value)->pushed x to the first stack
#push2(value)->pushed x to the second stack

#pop1()->pop an element out from the first stack
#             if the first stack is not empty
#pop2()->pop an element out from the second stack
#             if the first stack is not empty


from array1 import Array

class TwoStack:
    #Create an empty Stack using list.
    def __init__(self,maxSize):
        self._stack = Array(maxSize)
        self._capicity = maxSize
        self._top1 = -1
        self._top2 = maxSize

    #Judge the first Stack is empty or not.
    def isEmpty1(self):
        return self._top1  == -1

    #Judge the second Stack is empty or not.
    def isEmpty2(self):
        return self._top2  == self._capicity
    
    #Return the number of items in the first Stack. 
    def len1(self):
        return self._top1 + 1

    #Return the number of items in the second Stack.
    def len2(self):
        return self._capicity - self._top2
    
    #Add item in the first Stack.
    def push1(self,elem):
        assert self._top2 - self._top1 > 1,"the Stack is full"
        self._top1 += 1
        self._stack[self._top1] = elem

    #Add item in the second Stack.
    def push2(self,x):
        assert self._top2 - self._top1 > 1,"the Stack is full"
        self._top2 -= 1
        self._stack[self._top2] = x
            
    #Return the top item in the Stack after being sure the stack is not empty.
    def peek1(self):
        assert not self.isEmpty1(),"The first stack is empty"
        return self._stack[self._top1]

    #Return the top item in the Stack after being sure the stack is not empty.
    def peek2(self):
        assert not self.isEmpty2(),"The second stack is empty"
        return self._stack[self._top2]
    
    #Return and remove the top item in the Stack after being sure the stack is not empty.    
    def pop1(self):
        assert not self.isEmpty1(),"The first stack is empty"
        value =  self._stack[self._top1]
        self._top1 -= 1
        return value

    #Return and remove the top item in the Stack after being sure the stack is not empty.    
    def pop2(self):
        assert not self.isEmpty2(),"The second stack is empty"
        value =  self._stack[self._top2]
        self._top2 += 1
        return value
    
    #For debug:print stack1
    def str1(self):
        assert not self.isEmpty1(),"The first stack is empty"
        print "First Stack: ",
        for i in range(self._top1+1):
            print self._stack[i],

    def str2(self):
        assert not self.isEmpty2(),"The second stack is empty"
        print "Second Stack: ",
        for i in range(self._capicity-1,self._top2-1,-1):
            print self._stack[i],            
