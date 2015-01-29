#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20141229
#Chapter2: Array ADT
#------------------------------------------
#Implements the Array ADT using array capabilities of
#the ctypes module.
import ctypes

class Array:
    # Creates an array with size elements.
    def __init__(self,size):
        assert size > 0,"Array size must be greater than zero."
        self._size = size
        # Create the array structure using the ctypes module
        PyArrayType = ctypes.py_object * size
        self._elements  = PyArrayType()
        # Initialize each element
        self.clear(None)

    
    # Returns the size of the array
    def __len__( self ):
        return self._size

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert index >= 0 and index < len (self),"Array subscript out of range."
        return self._elements[ index ]

    # Puts the value in the array element at index position.
    def __setitem__(self,index,value):
        assert index >= 0 and index < len (self),"Array subscript out of range."
        self._elements[ index ] = value

    # Clears the array by setting each element to the given value.
    def clear(self,value):
        for i in range( len (self) ):
            self._elements[ i ] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator( self._elements )

# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self,theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

#------------------------------------------
        
# Implementation of the Array2D ADT using an array of arrays
class Array2D:
    def __init__(self,numRows,numCols):
        #Create a 1-D array to store an array reference for each row.
        self._theRows = Array( numRows )

        #Create the 1-D arrays for each row of the 2-D array.
        for i in range( numRows ):
            self._theRows[i]  = Array( numCols )

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0]) #either number in 0~numRows-1 is ok.

    def clear(self,value):
        for row in range( self.numRows() ):
            self._theRows[row].clear( value )

        #  gets the contents of the element at position[i,j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2 ,"Invald number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (row >= 0 and row < self.numRows and  \
                col >= 0 and col < self.numCols ),"Invald number of array subscripts."
        theldArray = self._theRows[row]
        return theldArray[col]
        
        # Sets the contents of the element at position[i,j]
    def __setitem__( self, ndxTuple,value ):
        assert len(ndxTuple) == 2 ,"Invald number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (row >= 0 and row < self.numRows and  \
                col >= 0 and col < self.numCols ),"Invald number of array subscripts."
        theldArray = self._theRows[row]
        theldArray[col] = value

#------------------------------------------
class MultiArray:
    # Creates a multi-dimensions array.
    def __init__( self, *dimensions):
        assert len(dimensions) > 1, "The array must have 2 or more dimensions."
        # The variable argument tuple contains the dim sizes.
        self._dims = dimensions
        # Compute the total number of elements in the array.
        size = 1
        for d in self._dims:
            assert d > 0, "the dimensions must be > 0"
            size *= d

        #Creates the 1-D array to store the elements.
        self._theElements = Array( size )
        # Create a 1-D array to store the equation factors
        self._factors = Array( len(dimensions) )
        self._computeFactors()

    # Returns the number of dimensions in the array.
    def numDims( self ):
        return len(self._dims)

    
    # Returns the number of the given dimension
    def length( self, dim ):
        assert dim >= 1 and dim <= len(self._dims),\
                "Dimension component out of range"
        return self._dims[dim-1]

    # Clears the array by setting all elements to the given value.
    def clear(self,value):
        self._theElements.clear(value)

    # getting the value by given index
    def __getitem__( self,ndxTuple ):
        assert len(ndxTuple) == len(self._dims),\
               "Invalid # of array subscripts."
        index = self._computeIndex( ndxTuple )
        #print index
        assert index is not None, "Array subscripts is out of range."
        return self._theElements[index]

    # Setting the value at given index
    def __setitem__( self, ndxTuple, value):
        assert len(ndxTuple) == len(self._dims),\
               "Invalid # of array subscripts."
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscripts is out of range."
        self._theElements[index] = value

    #Print fucntion directly
    def __str__(self):
        print "< ",
        for i in range(len(self._theElements)):
            print self._theElements[i],
        return " >"

    # Compute the offset in 1-D array by given idx
    def _computeIndex(self,idx):
        offset = 0
        for j in range(len(idx)):
            if idx[j] < 0 or idx[j] >= self._dims[j]:
                return None
            else:
                offset += idx[j] * self._factors[j]
                #print "idx[j] = ",idx[j]
                #print "offset..",offset
        #print "offset",offset
        return offset
        
    def _computeFactors(self):
        self._factors.clear(1)
        for i in range(len(self._dims)):
            #print "i = ",i
            for j in range(i+1,len(self._dims)):
                #print "j = ",j
                self._factors[i] *= self._dims[j]
            #print "self._factors[{}]".format(i),self._factors[i]
        

#------------------------------------------
class TriangleArray:
    # Creates a M x M TriangleArray.
    def __init__(self,numRow):
        self._theRows = numRow
        arraySize = self._computeSize()
        self._theElements = Array( arraySize )
        self._factors = Array( numRow )
        self._computeFactors()
    # Returns the rows of the TriangleArray
    def numRows(self):
        return self._theRows

    # Returns the cols of the TriangleArray
    def numCols(self):
        return self._theRows

    # Clears the array by setting all elements to the given value.
    def clear(self,value):
        self._theElements.clear( value )

    #  gets the contents of the element at position[i,j]
    def __getitem__( self, ndxTuple ):
        assert len(ndxTuple) == 2 ,"Invald number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (row >= 0 and row < self.numRows and  \
                col >= 0 and col < self.numCols and \
                row >= col),"Invald number of array subscripts."        
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscripts is out of range."
        return self._theElements[index]
        
    # Sets the contents of the element at position[i,j]
    def __setitem__( self, ndxTuple,value ):
        assert len(ndxTuple) == 2 ,"Invald number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert (row >= 0 and row < self.numRows and  \
                col >= 0 and col < self.numCols and \
                row >= col),"Invald number of array subscripts."        
        index = self._computeIndex( ndxTuple )
        assert index is not None, "Array subscripts is out of range."
        self._theElements[index] = value

##  #Print fucntion directly
    #* ** *** ****
##    def __str__(self):
##        print "< ",
##        for i in range(len(self._theElements)):
##            print self._theElements[i],
##        return " >"

    #Print fucntion as triangleArray
    #   *
    #   * * 
    #   * * *
    #   * * * *
    def __str__(self):
        index = 0
        for i in range(1,self.numRows()+1):
            while i>0:
                print self._theElements[index],
                index += 1
                i -= 1
            print ""
        return ""
        
    #compute the number of elements in the given size of TriangleArray.
    def _computeSize(self):
        size = 0
        for i in range(1,self._theRows + 1):
            size += i
        return size
    
    #compute the index int the array.    
    def _computeIndex(self,idx):
        offset = 0
        #print "idx",idx
        for i in range(idx[0]+1):
            offset = idx[1] +self._factors[i]
        #print "offset = {}".format(offset)
        return offset
    
    #compute the index int the array.    
    def _computeFactors(self):
        self._factors.clear(0)
        for i in range(self._theRows):
            #print "i = ",i
            for j in range(i):
                #print "j = ",j
                self._factors[i] += j+1
                #print "self._factors[{}] = {}".format(i,self._factors[i])
            
            #print "self._factors[{}]".format(i),self._factors[i]
