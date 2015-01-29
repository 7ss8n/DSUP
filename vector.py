#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150101
#Chapter2: Programing Projects2.1, Vector ADT using Array class.
#------------------------------------------
# Implement the Vector ADT using the Array class
from array1 import Array
from copy import deepcopy

class Vector:
    # Creates a Vector .
    def __init__(self,length = 2):
        self._vect = Array(length)
        self._capicity = len(self._vect)
        self._size = 0

    
    # Returns the size of the array
    def __len__( self ):
        return self._size    

    # Determines if the given item is contained in the vector.
    def contains(self,item):
        for i in range(len(self._vect)):
            if item == self._vect[i]:
                return True
        return False

    # Returns the item stored in the ndx element of the list.
    # The value of ndx must be within the valid range.
    def __getitem__(self,ndx):
        assert ndx >= 0 and ndx < len(self._vect),\
               "Vector subscript out of range."
        return self._vect[ndx]

    # Set the ndx element of the list to be the given value.
    # The value of ndx must be within the valid range.
    def __setitem__(self,ndx,value):
        assert ndx >= 0 and ndx < len(self._vect),\
               "Vector subscript out of range."
        self._vect[ndx] = value

    # Adds the given item to the end of the list.
    def append(self,item):
        if self._size >= self._capicity:
            #
            ##print "debug"
            oldVector = self._vect
            oldSize = self._size
            #
            self._vect = Array(2*oldSize)
            self._capicity = len(self._vect)
            for i in range(oldSize):
                self._vect[i] = oldVector[i]
            self._vect[oldSize] = item
            self._size += 1
        else:
            self._vect[self._size] = item
            self._size += 1

    # Inserts the given item in the element at position ndx
    def insert(self,ndx,item):
        if self._size >= self._capicity:
            print "debug"
            oldVector = self._vect
            oldSize = self._size
            #
            self._vect = Array(2*oldSize)
            self._capicity = len(self._vect)
            for i in range(ndx):
                self._vect[i] = oldVector[i]
            self._vect[ndx] = item
            for i in range(ndx+1,oldSize+1):
                self._vect[i] = oldVector[i-1]                
            self._size += 1
        else:
##            oldVector = Array(self._size)
##            for i in range(self._size):
##                oldVector[i] = self._vect[i]
            oldVector = deepcopy(self._vect)
            print "ndx = ",ndx
            print "item = ",item
            for i in range(ndx):
                print "i1 = ",i
                print "oldVector[i] = ",oldVector[i]
                self._vect[i] = oldVector[i]
            self._vect[ndx] = item
            for i in range(ndx+1,self._size+1):
                print "i2 = ",i
                print "oldVector[i-1] = ",oldVector[i-1]
                self._vect[i] = oldVector[i-1]                
            self._size += 1             
        
    
        
