#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter6: Linked Structures
#------------------------------------------
#Implements the Polynomial ADT using LinkList

class Polynomial:
    #Initail the Polynomial
    def __init__(self,degree = None,cofficient = None):
        if degree != None:
            NewNode = _PolynomialListNode(degree,cofficient)
            self._PolynomialHead = NewNode
        else:
            self._PolynomialHead = None
        self._PolynomialTail = self._PolynomialHead
        

    def degree(self):
        if self._PolynomialHead is None:
            return -1
        else:
            return self._PolynomialHead.degree

    def __getitem__(self,degree):
        assert self.degree>=0,"Operation not permitted on an empty polynomial."
        curNode  = self._PolynomialHead
        while curNode is not None and curNode.degree > degree:
            curNode = curNode.next
        #print "curNode.degree",curNode.degree
        if curNode is None or curNode.degree != degree :
            return 0.0
        else:
            return curNode.cofficient

    def evaluate(self, scalar):
        assert self.degree>=0,"Operation not permitted on an empty polynomial."
        curNode  = self._PolynomialHead
        total = 0.0
        while curNode is not None :
            total += curNode.cofficient*(scalar**curNode.degree)
            curNode = curNode.next
        return total

    def _appendTerms(self,degree,cofficient):
        if cofficient != 0.0:
            NewNode = _PolynomialListNode(degree,cofficient)
            if self._PolynomialHead is None:
                self._PolynomialHead = NewNode
            else:
                self._PolynomialTail.next =  NewNode
            self._PolynomialTail = NewNode

    def __add__(self,rhsPoly):
        
        

class _PolynomialListNode:
    def __init__(self,degree,cofficient):
        self.degree = degree
        self.cofficient = cofficient
        self.next = None

        
