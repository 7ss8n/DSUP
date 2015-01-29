#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150129
#Chapter1: ADT
# Programming Projects 1.3
#Counting Bag ADT
#------------------------------------------
#Implements the Counting Bag ADT using ADT.

class CountBag:
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)
    
    def __contains__(self,item):
        return item in self._theElements

    def add(self,item):
        self._theElements.append(item)

    def remove(self,item):
        #print item
        assert item in self._theElements,"There is no item in the Bag."
        ndx = self._theElements.index(item)
        return self._theElements.pop(ndx)

    def numOf(self,item):
        assert item in self._theElements,"There is no item in the Bag."
        count = 0
        for elem in self._theElements:
            if item == elem:
                count +=1 
        return count   
        
        

def main():
    myBag = CountBag()
    myBag.add( 19 )
    myBag.add( 74 )
    myBag.add( 23 )
    myBag.add( 19 )
    myBag.add( 12 )

##    value = int( input("Guess a value contained in the bag.") )
##    if value in myBag:
##        print( "The bag contains the value", value )
##    else :
##        print( "The bag does not contain the value", value )

    print myBag.remove(74)
    print myBag.numOf(19)

main()
