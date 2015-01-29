#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter6: Linked Structures
#------------------------------------------
#Implements the Bag ADT using LinkList

class Bag:
    #Constructs an empty bag.
    def __init__(self):
        self._head = None
        self._size = 0
        
    #Return the number of items in the bag.
    def __len__(self):
        return self._size

    #Determines if an item is contained in the Bag.
    def __contains__(self,target):
        curNode = self._head
        while curNode is not None and curNode.item !=target:
            curNode = curNode.next
        return curNode is not None
    
    #Add item to the Bag.
    def add(self,item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    #Remove item from the Bag.    
    def remove(self,item):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None, "The item must be in the Bag."
                
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        self._size -= 1
        
        return curNode.item

    def __str__(self):
        curNode = self._head
        while curNode is not None:
            print curNode.item,
            curNode = curNode.next
        return ""
        

    def __iter__(self):
        return _BagIterator(self._head)
        

class _BagListNode:
    def __init__(self,item):
        self.item = item
        self.next = None

class _BagIterator:
    def __init__(self,listHead):
        self._curNode = listHead

    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
