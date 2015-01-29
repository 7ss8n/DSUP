#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter11: Hash Tables
#------------------------------------------
#Implements the Map ADT using closed hashing and 
#a probe with double hashing
from array1 import Array

class _MapEntry:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
class HashMap:
    #Defines constants to represent the status of each table entry
    UNUSED = None
    EMPTY = _MapEntry(None, None)
    INIT_SIZE = 7

    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - len(self._table)/3

    def __len__(self):
        return self._count

    def __contains__(self,key):
        slot = self._findSlot(key,False)
        return slot is not None

    def add(self,key,value):
        if key in self:
            slot = self._findSlot(key,False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key,True)
            print "slot = ",slot
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True
    def valueOf(self,key):
        slot = self._findSlot(key,False)
        assert slot is not None,"Invalid map key"
        return self._table[slot].value

    def _findSlot(self,key,forInsert):
        slot = self._hash1(key)
        #print "hash1:slot = ",slot
        step = self._hash2(key)

        M = len(self._table)
        print "self.UNUSED = ",self.UNUSED
        while self._table[slot] is not self.UNUSED:
            if forInsert and \
               (self._table[slot] is self.UNUSED or self._table[slot] is self.EMPTY):
                return slot
            elif not forInsert and \
               (self._table[slot] is not self.UNUSED and self._table[slot] is not self.EMPTY):
                return slot
            else:
                slot = (slot +step) % M
        return slot

    def _rehash(self):
        #Create a new larger hash table.
        origTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array(newSize)

        #modify the size attributes.
        self._count = 0
        self._maxCount = len(self._table) - len(self._table)/3
        for entry in origTable:
            if entry is not self.UNUSED and entry is not self.EMPTY:
                slot = self._findSlot(entry.key,True)
                self._table[slot] = entry
                self._count += 1

    def _hash1(self,key):
        return abs(hash(key))%len(self._table)

    def _hash2(self,key):
        return 1 + abs(hash(key))% ( len(self._table) - 2 )


#
