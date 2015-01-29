#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter14: Search Trees
#------------------------------------------
#Implements the Map ADT using binary search tree.

class BSTMap:
    #creates an empty map instance.
    def __init__(self):
        self._root = None
        self._size = 0

    #return the size of BSTMap
    def __len__(self):
        return self._size

    def __iter__(self):
        return _BSTMapIterator(self._root)

    #judge the kye is in Map or not,return True or False.
    def __contains__(self,key):
        return self._bstSearch(self._root,key) is not None

    #return the kye's value in Map or return invalid key.
    def valueOf(self,key):
        node = self._bstSearch(self._root,key)
        assert node is not None,"Invalid map key"
        return node.value

    #Add a new element in the map
    def add(self,subtree,key,value):
        node = self._bstSearch(self._root,key)
        if node is not None:
            node.value = value
            return False
        else:
            self._root = self._bstInsert(self._root,key,value)
            self._size += 1
            return True

    def remove(self,subtree,key):
        node = self._bstSearch(self._root,key)
        assert node is not None,"Invalid map key"
        self._root = self._bstRemove(self._root,key)
        self._size -= 1

    #Helper function:find the target key's Tree Node.
    def _bstSearch(self,subtree,target):
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._bstSearch(subtree.left,target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right,target)
        else:
            return subtree
        
    #Return the minimum value in Map
    def _bstMinimum(self,subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinumum(subtree.left)

    #Return the maximum value in Map
    def _bstMaximum(self,subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bstMaxium(self,subtree.right)

    #Helper function:Insert a new given element.
    def _bstInsert(self,subtree,key,value):
        if subtree is None:
            subtree = _BSTMapNode(key,value)
        elif key<subtree.key:
            subtree.left = self._bstInsert(subtree.left,key,value)
        elif key<subtree.key:
            subtree.right = self._bstInsert(subtree.right,key,value)
        return subtree

    #Helper function:Remove  given key's Node.
    def _bstRemove(self,subtree,target):
        if subtree is None:
            return None
        elif target < subtree.key:
            subtree.left =  self._bstRemove(subtree.left,target)
            return subtree
        elif target > subtree.key:
            subtree.right =  self._bstRemove(subtree.right,target)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self._bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.valu
                subtree.right = self._bstRemove(subtree.right,successor.key)
                return subtree

            
class _BSTMapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    

