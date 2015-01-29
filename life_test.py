#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150101
#Chapter2: Life Game ADT Test module
#------------------------------------------

from life import LifeGrid

#Define the initial configuraton of live cells

INIT_CONFIG = [ (1,2), (2,1), (2,2), (2,3) ]
####for test 7th generation
##INIT_CONFIG = [(0,2),\
##               (1,1),(1,2),(1,3), \
##               (2,0),(2,1),(2,3),(2,4),\
##               (3,1),(3,2),(3,3), \
##               (4,2)]

##---------------exercise 2.5
##a)
##INIT_CONFIG = [(1,3),\
##               (2,2),\
##               (3,1)]

#b)
INIT_CONFIG = [(0,0),(0,4),\
               (1,1),(1,3), \
               (2,2),\
               (3,1),(3,3), \
               (4,0),(4,4)]
#c)
INIT_CONFIG = [(0,1),(0,3),\
               (1,1),(1,3),\
               (2,1),(2,3), \
               (3,1),(3,3),\
               (4,0),(4,1),(4,3),(4,4)]
#d)
INIT_CONFIG = [(0,0),(0,1),(0,2),(0,3),(0,4),\
               (1,0),(1,1),(1,2),(1,3),(1,4),\
               (2,0),(2,1),(2,2),(2,3),(2,4), \
               (3,0),(3,1),(3,2),(3,3),(3,4),\
               (4,0),(4,1),(4,2),(4,3),(4,4)]

#e)
INIT_CONFIG = [(0,2),\
               (1,2),\
               (2,0),(2,1),(2,2),(2,3),(2,4), \
               (3,2),\
               (4,2),]

#f)
INIT_CONFIG = [(0,0),(0,1),(0,3),(0,4),\
               (1,1),(1,3),\
                \
               (3,1),(3,3),\
               (4,0),(4,1),(4,3),(4,4)]
#set the size of the gird.
GRID_WIDTH = 5
GRID_HEIGHT = 5

#Indicate the number of generations.
NUM_GENS = 8

def main():
    ## prompt the user for the grid size and generations
    GRID_WIDTH = int(raw_input("Enter the width of grid:>>>"))
    GRID_HEIGHT = int(raw_input("Enter the height of grid:>>>"))
    NUM_GENS = int(raw_input("Enter the generations of grid:>>>"))
    #Construct the game grid and configure it.
    grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT)
    grid.configure( INIT_CONFIG )

    # generate the next generation of organisms
    def evolve ( grid ):
        #List for storing the live cells of the next generation.
        liveCells = list()

        for i in range(grid.numRows()):
            for j in range(grid.numCols()):
                neighbors = grid.numLiveNeighbors( i , j)
                ##print "(i,j)=(",i,",",j,") ","neighbors= ",neighbors
                
                if ( neighbors == 2 and grid.isLive(i,j)) or\
                   ( neighbors == 3 ):
                    liveCells.append((i,j))
        
        grid.configure(liveCells)

    def draw ( grid ):
        for i in range(grid.numRows()):
            for j in range(grid.numCols()):
                if grid.isLive(i,j):
                    print "@",
                else:
                    print ".",
            print ""

    #Start the game.
    print "Generation = ",0
    draw(grid)
    for i in range( NUM_GENS ):
        print "Generation = ",i+1
        evolve ( grid )
        draw(grid)


    

# Executes the main routine.
main()
