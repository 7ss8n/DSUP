#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150102
#Chapter3: Map ADT
#------------------------------------------
#Implementation of the Map ADT using a list
from array1 import Array
class Map:
    #Creates an empty map instance.
    def __init__(self):
        self._entryList = list()

    #Returns the number of entries in the map
    def __len__(self):
        return len(self._entryList)

    #Determines if the map contains the given key.
    def __contains__(self, key):
        ndx = self._findPosition( key )
        return ndx is not None


    # new value replaces the current value associated with the key
    def add(self,key,value):
        ndx = self._findPosition( key )
        if ndx is not None:
            #renew the value
            self._entryList[ndx].value = value
            return False
        else:
            newEntry = _MapEntry(key,value)
            self._entryList.append(newEntry)
            return True

    # remove the given key from the map
    def remove(self,key):
        ndx = self._findPosition( key )
        print "ndx = ",ndx
        assert ndx != None,"the key is not in the map"
        #entry = _MapEntry(key,self._entryList[ndx].value)
        #print "entry.key",entry.key
        #print "entry.value",entry.value
        #print entry
        #print entry is self._entryList[ndx]
        ###self._entryList.remove(entry)
        #error: because entry is not the sama as self._entryList[ndx]
        #Only the value and key is the same ,object is not the same
        #We can verify it using : print entry is self._entryList[ndx],
        #returning false
        self._entryList.pop(ndx)

    # Returns the data record associated with the given key.
    def valueOf(self,key):
        ndx = self._findPosition( key )
        assert ndx != None,"the key is not in the map"
        return self._entryList[ndx].value   

    #Find the key's position in map
    def _findPosition(self,key):
        for ndx in range(len(self._entryList)):
            if self._entryList[ndx].key == key:
                return ndx
        return None
    
    # Returns an iterator for traversing the items in map.      
    def __iter__(self):
        return _MapIterator( self._entryList )

    # returns the key array in the map
    def keyArray(self):
        keyArray = Array(len(self._entryList))
        for ndx in range(len(self._entryList)):
            keyArray[ndx] = self._entryList[ndx].key    
        return keyArray
    
    # new value replaces the current value associated with the key
    def __setitem__(self,key,value):
        ndx = self._findPosition( key )
        if ndx is not None:
            #renew the value
            self._entryList[ndx].value = value
            return False
        else:
            newEntry = _MapEntry(key,value)
            self._entryList.append(newEntry)
            return True
    # Returns the data record associated with the given key.
    def __getitem__(self,key):
        ndx = self._findPosition( key )
        assert ndx != None,"the key is not in the map"
        return self._entryList[ndx].value 
    

# An iterator for the Array ADT.
class _MapIterator:
    def __init__(self,theMap):
        self._mapRef = theMap
        self._curNdx = 0

    def __iter__(self):
        return self

    def next(self):
        if  self._curNdx < len(self._mapRef):
            entry = self._mapRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration             

#Class to store the key and value pairs.
class _MapEntry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

        
        
        
