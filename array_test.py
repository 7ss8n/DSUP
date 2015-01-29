from array1 import Array
from array1 import Array2D
from array1 import MultiArray
from array1 import TriangleArray
##size = 10
##A = Array(size)
##
##for i in range(size):
##    A[i] = i
##    print 's[{}] = {}'.format(i,A[i])
##
##for value in A:
##    print value
##
##A.clear(None)
##for i in range(size):
##    print 's[{}] = {}'.format(i,A[i])
##    
##print 'Array length = ',len(A)

# Create an array for the counters and initialize each element to zero.
##theCounters = Array( 256 )
##theCounters.clear(0)

#open the text file for reading and extract each line from the file
#and iterate over each character in the line.

##theFile = open('atextfile.txt','r')
##
##for line in theFile:
##    for letter in line:
##        code = ord(letter)
##        theCounters[code] +=1
##
###close the file
##theFile.close()
##
##for i in range(26):
##    print("%c - %4d     %c - %4d"%\
##          (chr(65+i),theCounters[65+i],chr(97+i),theCounters[97+i]))

def array2D_test():
    rows = 2
    cols = 3
    A2d = Array2D(rows,cols)
    for row in range(A2d.numRows()):
        for col in range(A2d.numCols()):
            A2d[row,col] = row + col

    def print_array2d(array2d):
        for row in range(array2d.numRows()):
            print "row = ",row
            for col in range(array2d.numCols()):
                print array2d[row,col],
            print ""

            
    print_array2d(A2d)

    A2d.clear(10)
    print_array2d(A2d)


#call
#array2D_test()


def multiArray_test():
    d1 = 2
    d2 = 3
    d3 = 4
    MDArray = MultiArray(d1,d2,d3)
    MDArray.clear(1)
    print "the number of Dims: ",MDArray.numDims()
    print "the length of Dim 1: ",MDArray.length(1)
    print "the length of Dim 2: ",MDArray.length(2)
    print "the length of Dim 3: ",MDArray.length(3)

    for i in range( MDArray.length(1) ):
        for j in range( MDArray.length(2) ):
            for k in range( MDArray.length(3) ):
                MDArray[i,j,k] = i + j + k
    for i in range( MDArray.length(1) ):
        for j in range( MDArray.length(2) ):
            for k in range( MDArray.length(3) ):
                print "MDArray[{},{},{}] = ".format(i,j,k),MDArray[i,j,k]

    print MDArray
    
    for i in range(len(MDArray._theElements)):
        print MDArray._theElements[i],
    
#call
#multiArray_test()


def TriangleArray_test():
    TriaArray = TriangleArray(12)
    TriaArray.clear(1)
    print TriaArray[2,1]
    print TriaArray

    tempValue = 0
    for i in range(TriaArray.numRows()):
        for j in range(i+1):
            tempValue += 1
            TriaArray[i,j] = tempValue
    print TriaArray
#call
TriangleArray_test()
