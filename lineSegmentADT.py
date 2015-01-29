#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150129
#Chapter1: ADT
# Programming Projects 1.8
#Line Segment ADT
#------------------------------------------
#Implements the Line Segment ADT using Point ADT.
from math import sqrt

class LineSegment:
    def __init__(self,ptA,ptB):
        self._endPontA = ptA
        self._endPontB = ptB

    def endPointA(self):
        return "({},{})".format(self._endPontA.getX(),self._endPontA.getY())
        #print  self._endPontA

    def endPointB(self):
        return "({},{})".format(self._endPontB.getX(),self._endPontB.getY())
        #print  self._endPontB
        
    def length(self):
        return self._endPontA.distance(self._endPontB)

    def isVertical(self):
        return self._endPontA.getX() == self._endPontB.getX()

    def isHorizontal(self):
        return self._endPontA.getY() == self._endPontB.getY()

    def slope(self):
        if not self.isVertical():
            return (self._endPontA.getY() - self._endPontB.getY())/(self._endPontA.getX() - self._endPontB.getX())

    def isParallel(self,otherLine):
        if self.isVertical() and otherLine.isVertical():
            return True
        elif not self.isVertical() and not otherLine.isVertical():
            return self.slope() == otherLine.slope()
        else:
            return False

    def isPerpendicular(self,otherLine):
        if self.isVertical() and otherLine.isHorizontal():
            return True
        elif self.isHorizontal() and otherLine.isVertical():
            return True
        elif not self.isVertical() and not otherLine.isVertical():
            return self.slope() * otherLine.slope() == -1
        else:
            return False
                        
    def intersects(self,otherLine):
        return not self.isParallel(otherLine)

    def shift(self,xInc,yInc):
        self._endPontA.shift(xInc,yInc)
        self._endPontB.shift(xInc,yInc)

    def midPoint(self):
        midX = (self._endPontA.getX() + self._endPontB.getX())/2
        midY = (self._endPontA.getY() + self._endPontB.getY())/2
        mid = Point(midX,midY)
        print mid
                        

    def __str__(self):
        return "({0},{1})#({2},{3})".format(self._endPontA._x,self._endPontA._y,\
                                            self._endPontB._x,self._endPontB._y)
    
        

class Point:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def distance(self,otherPoint):
        dx = self.getX() - otherPoint.getX()
        dy = self.getY() - otherPoint.getY()
        return sqrt(dx**2 + dy**2)

    def shift(self,xInc,yInc):
        self._x += xInc
        self._y += yInc                

    def __str__(self):
        return "({},{})".format(self._x,self._y)
        
        
def main():
    PointOrig = Point(0,0)
    PointA = Point(3,4)
    PointB = Point(6,8)
    PointC = Point(3,0)
    PointD = Point(0,3)
    line1 = LineSegment(PointA,PointOrig)
    line2 = LineSegment(PointC,PointOrig)
    line3 = LineSegment(PointD,PointOrig)
    line4 = LineSegment(PointB,PointOrig)
    
    print "x of PointA:",PointA.getX()
    #PointA.distance(PointB)
    print "line1 = ",line1
    print "line2 = ",line2
    print "line3 = ",line3
    print "line4 = ",line4
    
    print "line1's distance = ",line1.length()
    print "line1's endPointA = ",line1.endPointA()    
    print "line1's endPointB = ",line1.endPointB()
    
    print "line1{} is Vertical? {}".format(line1,line1.isVertical())
    print "line2{} is Vertical? {}".format(line2,line2.isVertical())
    print "line3{} is Vertical? {}".format(line3,line3.isVertical())
    print "line4{} is Vertical? {}".format(line4,line4.isVertical())
    
    print "line1{} is Horizontal? {}".format(line1,line1.isHorizontal())
    print "line2{} is Horizontal? {}".format(line2,line2.isHorizontal())
    print "line3{} is Horizontal? {}".format(line3,line3.isHorizontal())
    print "line4{} is Horizontal? {}".format(line4,line4.isHorizontal())

    print "line1{} and line2{} is Parallel? {}".format(line1,line2,line1.isParallel(line2))
    print "line3{} and line2{} is Parallel? {}".format(line3,line2,line3.isParallel(line2))
    print "line1{} and line4{} is Parallel? {}".format(line1,line4,line1.isParallel(line4))    

main()
