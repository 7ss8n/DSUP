#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150101
#Chapter2: Life Game ADT
#------------------------------------------
#Implementation of the Life Game ADT using an Array2D
from array1 import Array2D

class LifeGrid :
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__( self, numRows, numCols ):
        # Allocate the 2-D array for the grid.
        self._grid = Array2D( numRows, numCols )
        #Clear the grid and set all cells to dead.
        self.configure(list())

    # return the number of rows in the grid.
    def numRows( self ):
        return self._grid.numRows()

    # return the number of columns in the grid.
    def numCols( self ):
        return self._grid.numCols()

    # according the given list:set the coordList to live.
    def configure( self , coordList ):
        #clear the gird first
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i,j)
        #set the indicated cells to be alive.
        for coord in coordList:
            ##print "corrd = ",coord
            self.setCell(coord[0],coord[1])

    # set the given gird to dead.
    def clearCell(self,row,col):
            self._grid[row,col] = LifeGrid.DEAD_CELL

    # set the given gird to live.
    def setCell(self,row,col):
        self._grid[row,col] = LifeGrid.LIVE_CELL

    # judge the given grid is live or not.
    def isLive(self,row,col):
        return self._grid[row,col] == LifeGrid.LIVE_CELL

    # to count the given grid's live neighbors
    def numLiveNeighbors(self, row, col):
        count = 0
        # assert boundary
        if row - 1 < 0:
            row1 = 0
        else:
            row1 = row - 1

        if row + 1 > (self.numRows()-1):
            row2 = self.numRows()
        else:
            row2 = row + 2    
                
        if col - 1 < 0:
            col1 = 0
        else:
            col1 = col - 1

        if col + 1 > (self.numCols()-1):
            col2 = self.numCols()
        else:
            col2 = col + 2    
        ##print "(row1,row2)=(",row1,",",row2,") "
        ##print "(col1,col2)=(",col1,",",col2,") "
        # judge the live neighbors  
        for i in range(row1,row2):
            for j in range(col1,col2):
                if((i,j)!=(row,col) and self.isLive(i,j)):
                    count += 1
        return count
            

        

