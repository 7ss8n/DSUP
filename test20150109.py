class _BagIterator:
    def __init__(self,theList):
        self._bagItems = theList
        self._curTtem = 0

    def __iter__(self):
        return self

    ##Python 3.x __next__()
    ##Python 2.x   next()
    def next(self):
        if self._curItem < len( self._bagItems ):
            item = self._bagItems[self._curItem]
            self._curItem += 1
            return item
        else:
            raise StopIteration
