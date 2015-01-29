#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150129
#Chapter1: ADT
# Programming Projects 1.2
#Grab Bag ADT
#------------------------------------------
#Implements the Grab Bag ADT using ADT.
from random import randint

class GrabBag:
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)
    
    def __contains__(self,item):
        return item in self._theElements

    def add(self,item):
        self._theElements.append(item)

    def getItem(self):
        numOfItems = len(self._theElements)
        assert numOfItems>0,"There is no item in the Bag."
        ndx = randint(0,numOfItems-1)
        return self._theElements.pop(ndx)
        
        

def main():
    myBag = GrabBag()
    myBag.add( 19 )
    myBag.add( 74 )
    myBag.add( 23 )
    myBag.add( 19 )
    myBag.add( 12 )

    value = int( input("Guess a value contained in the bag.") )
    if value in myBag:
        print( "The bag contains the value", value )
    else :
        print( "The bag does not contain the value", value )

    print myBag.getItem()
    print myBag.getItem()
    print myBag.getItem()
    print myBag.getItem()
    print myBag.getItem()
    #print myBag.getItem()

main()
