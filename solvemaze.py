#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150120
#Chapter7: Stack Structures
#------------------------------------------
#Soving maze problem

from array1 import Array2D
from lliststack import Stack

class Maze:
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"
    def __init__(self,numRows,numCols):
        self._mazeCells = Array2D( numRows, numCols )
        self._startCell = None
        self._exitCell = None

    def numRows(self):
        return self._mazeCells.numRows()

    def numCols(self):
        return self._mazeCells.numCols()

    def setWall(self,row,col):
        assert row>=0 and row <= self.numRows() and \
               col>=0 and col <= self.numCols(),\
               "Cell index out of Range."
        self._mazeCells[row,col] = self.MAZE_WALL

    def setStart(self,row,col):
        assert row>=0 and row <= self.numRows() and \
               col>=0 and col <= self.numCols(),\
               "Cell index out of Range."
        self._startCell = _CellPosition(row,col)

    def setExit(self,row,col):
        assert row>=0 and row <= self.numRows() and \
               col>=0 and col <= self.numCols(),\
               "Cell index out of Range."
        self._exitCell = _CellPosition(row,col)

    def findPath(self):
        row = self._startCell._row
        col = self._startCell._col
        while True:
            if self._validMove(row,col):
                _markPath(self,row,col)
                row = row -1
            else:
                col = col -1
        return

    def reset(self):
        return

    def draw(self):
        return
    
    def _validMove(self,row,col):
        return row>=0 and row <= self.numRows() and \
               col>=0 and col <= self.numCols() and \
               self._mazeCells[row,col] is None

    def _exitFound(self,row,col):
        return row = self._startCell._row and \
                     col = self._startCell._col

    def _markTried(self,row,col):
        assert row>=0 and row <= self.numRows() and \
               col>=0 and col <= self.numCols(),\
               "Cell index out of Range."
        self._mazeCells[row,col] = self.TRIED_TOKEN
                
    def _markPath(self,row,col):
        assert row>=0 and row <= self.numRows() and \
               col>=0 and col <= self.numCols(),\
               "Cell index out of Range."
        self._mazeCells[row,col] = self.PATH_TOKEN                     

    


class _CellPosition:
    def __init(row,col):
        self._row = row
        self._col = col

        
