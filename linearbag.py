#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150127
#Chapter1: ADT
#------------------------------------------
#Implements the Bag ADT using Python list.

class Bag:
    #Constructs an empty Bag.
    def __init__(self):
        self._theItems = list()

    #Returns the number of items in Bag.
    def __len__(self):
        return len(self._theItems)

    #Judge given item in the Bag or not.
    def __contains__(self,item):
        return item in self._theItems

    #Add a new item in the Bag.
    def add(self,item):
        self._theItems.append(item)

    #Remove and return an item from the Bag.
    def remove(self,item):
        assert item in self._theItems,"Item is not in the Bag."
        ndx = self._theItems.index(item)
        print "ndx = ",ndx
        itemToRemove = self._theItems.pop(ndx)
        print self._theItems
        return itemToRemove

    def __iter__(self):
        return _BagIterator(self._theItems)

    
class _BagIterator:
    def __init__(self,theList):
        self._bagItems = theList
        self._curItem = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curItem < len(self._bagItems):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
    


#testcase
def main():
    myBag = Bag()
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

    for item in myBag:
        print "item = ",item
        itemToRemove = myBag.remove(item)
        print "after remove:",itemToRemove
        print "len = ",len(myBag)

#call
main()
