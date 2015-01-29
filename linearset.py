# -*- coding: cp936 -*-
#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150102
#Chapter3: Set ADT
#------------------------------------------
#Implementation of the Set ADT using a list

class Set:
    # Create an empty set instance
    def __init__( self ,*initElements):
        self._theElements = list()
        if(len(initElements)!= 0):
            for i in range(len(initElements)):
              self._theElements.append(initElements[i])  

    # Return the number of items in the set
    def __len__( self ):
        return len( self._theElements )

    # Judge if an element is in the set
    def __contains__( self, element ):
        return element in self._theElements

    # Judge if the set is empty
    def isEmpty( self ):
        return len( self._theElements ) == 0

    # Adds a new unique element to the set
    def add( self, element ):
        if element not in self._theElements:
            self._theElements.append(element)

    # Removes an element from the set.
    def remove( self, element ):
        assert element in self._theElements,\
               "The element is not in the set."
        self._theElements.remove( element )

    # Determines if two sets are equal.
    def __eq__( self, setB ):
        if len(self) != len(setB):
            return False
        else:
            for elem in self:
                if elem not in setB:
                    return False
            return True

    # Determines if this set is a subset of setB.
    def isSubsetOf( self, setB ):
        for elem in self:
                if elem not in setB:
                    return False
        return True
    # Determines if this set is a subset of setB using less than
    def __lt__( self, setB ):
        for elem in self:
                if elem not in setB:
                    return False
        return True
    
    # Determines if this set is a subset of setB.
    def isProperSubsetOf( self, setB ):        
        if self.isSubsetOf(setB) and (not(self == setB)):
            #error: self!=setB return True???
            return True
        else:
            return False
    

    # Creates a new set from the union of this set and setB.
    def union( self, setB ):
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for elem in setB:
            if elem not in self:
                newSet._theElements.append( elem )
        return newSet
    
    # Creates a new set from the union of this set and setB using add operator
    def __add__( self, setB ):
        newSet = Set()
        newSet._theElements.extend( self._theElements )
        for elem in setB:
            if elem not in self:
                newSet._theElements.append( elem )
        return newSet

    # Creates a new set from the intersection: self set and setB.
    def intersect( self, setB ):
        newSet = Set()
        for elem in self:
            if elem  in setB:
                newSet._theElements.append( elem )
        return newSet
    # Creates a new set from the intersection: self set and setB using multiply operator
    def __mul__( self, setB ):
        newSet = Set()
        for elem in self:
            if elem  in setB:
                newSet._theElements.append( elem )
        return newSet
    
    # Creates a new set from the difference: self set and setB.
    def difference( self, setB ):
        newSet = Set()
        for elem in self:
            if elem  not in setB:
                newSet._theElements.append( elem )
        return newSet    
    # Creates a new set from the difference: self set and setB using sub 
    def __sub__( self, setB ):
        newSet = Set()
        for elem in self:
            if elem  not in setB:
                newSet._theElements.append( elem )
        return newSet

    def _str(self):
        print"<",
        for elem in self:
            print elem,
        print ">"

    def __str__(self):
        print"<",
        for elem in self:
            print elem, 
        return " >"
        
    # Returns an iterator for traversing the items in set.      
    def __iter__(self):
        return _SetIterator( self._theElements )

# An iterator for the Array ADT.
class _SetIterator:
    def __init__(self,theSet):
        self._setRef = theSet
        self._curNdx = 0

    def __iter__(self):
        return self

    def next(self):
        if  self._curNdx < len(self._setRef):
            entry = self._setRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration    

    
