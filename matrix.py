#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20141229
#Chapter2: Matrix ADT
#------------------------------------------
#Implementation of the Matrix ADT using an Array2D
from array1 import Array2D

class Matrix:
    def __init__( self, numRows, numCols ):
        self.__theMatrix = Array2D( numRows, numCols )
        self.__theMatrix.clear( 0 )

    def numRows(self):
        return self.__theMatrix.numRows()

    def numCols(self):
        return self.__theMatrix.numCols()

    def clear(self,value):
        self.__theMatrix.clear( value )

    def __getitem__( self, ndxTuple ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        return self.__theMatrix[row,col]

    def __setitem__( self, ndxTuple ,value ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        self.__theMatrix[row,col] = value

    def scaleBy(self,scalar):
        for row in range(self.__theMatrix.numRows()):
            for col in range(self.__theMatrix.numCols()):
                self.__theMatrix[row,col] *= scalar

    def transpose(self):
        newMatrix = Matrix(self.numCols(), self.numRows())
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                newMatrix[col,row] = self.__theMatrix[row,col]
        return newMatrix

    def __add__(self,rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(),\
               "Matrix sizes not compatible for the add operation."
        newMatrix = Matrix( self.numRows(), self.numCols() )
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                newMatrix[row,col] = self[row,col] + rhsMatrix[row,col]
        return newMatrix

    def __sub__(self,rhsMatrix):
        assert self.numRows() == rhsMatrix.numRows() and \
               self.numCols() == rhsMatrix.numCols(),\
               "Matrix sizes not compatible for the sub operation."
        newMatrix = Matrix( self.numRows(), self.numCols() )
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                newMatrix[row,col] = self[row,col] - rhsMatrix[row,col]
        return newMatrix

    def __mul__(self,rhsMatrix):
        assert self.numCols() == rhsMatrix.numRows() , \
               "Matrix sizes not compatible for the multiply operation."
        newMatrix = Matrix( self.numRows(), rhsMatrix.numCols() )
        for row in range(self.numRows()):
            for col in range(rhsMatrix.numCols()):
                for i in range(self.numCols()):
                    newMatrix[row,col] += self[row,i] * rhsMatrix[i,col]
        return newMatrix        
    
