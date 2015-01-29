#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150122
#Chapter10: Recursion
#------------------------------------------

#####Example 01

def printRev(n):
    if n >0 :
        print n
        printRev(n-1)


#printRev(10)

def printInc(n):
    if n >0 :
        printInc(n-1)
        print n
        
#printInc(10)


def Factorials(n):
    assert n >=0,"Factorial not defined for negitive values"
    if n <2 :
        return 1
    else:
        return n * Factorials(n-1)

def Factorials_iter(n):
    assert n >=0,"Factorial not defined for negitive values"
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
        
##print Factorials(5)
##print Factorials(0)
##print Factorials(1)
##
##print Factorials_iter(5)
##print Factorials_iter(0)
##print Factorials_iter(1)

def main():
    y = foo(3)
    printRev(2)

def foo(n):
    if n%2 !=0 :
        return 0
    else :
        return foo(n-1) + n

#main()


def fabonacci(n):
    if n<2:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)
#test    
##for i in range(10):
##    print fabonacci(i)

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def buildLinkedList():
    head = ListNode(0)
    for i in range(1,10):
        newNode = ListNode(i)
        newNode.next = head
        head = newNode
        #print head.data
    return head

# Print the contents of a singly linked list in reverse order.
def PrintLikedListReverse(head):
    curNode = head
    num = 0
    while curNode is not None:
        num += 1
        curNode = curNode.next
    #print "num = ",num
    for i in range(num):
        count = num - i-1
        curNode = head
        #print "head,",curNode.data 
        for j in range(count):
            curNode = curNode.next
        print curNode.data

from pylistStack import Stack
def PrintLikedListReverse1(head):
    s = Stack()
    curNode = head
    while curNode is not None:
        s.push(curNode.data)
        curNode = curNode.next
    while not s.isEmpty():
        print (s.pop())
    

def PrintLikedListReverse2(head):
    curNode = head
    if curNode is not None:
        PrintLikedListReverse2(curNode.next)
        print curNode.data


    
    
       
def PrintList_test():
    head = buildLinkedList()
    print "PrintLikedListReverse"
    PrintLikedListReverse(head)
    print "PrintLikedListReverse1"
    PrintLikedListReverse1(head)
    print "PrintLikedListReverse2"
    PrintLikedListReverse2(head)

#PrintList_test()    



def recurBinarySearch(first,last,lst,value):
    if first>last:
        return False
    else:
        mid = (first + last)/2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            return recurBinarySearch(mid+1,last,lst,value)
        else:
            return recurBinarySearch(first,mid-1,lst,value)
#test
##lst = [i for i in range(10)]
##first = 0
##last = 9
##value = 5
##print recurBinarySearch(first,last,lst,value)
##value = 0
##print recurBinarySearch(first,last,lst,value)
##value = 9
##print recurBinarySearch(first,last,lst,value)
##value = 10
##print recurBinarySearch(first,last,lst,value)

def hanoitower(src,dest,mid,n):
    if n >= 1:
        hanoitower(src,mid,dest,n-1)
        print "Move {0} {1} to {2}".format(n,src,dest)
        hanoitower(mid,dest,src,n-1)

src = "A"
dest = "C"
mid = "B"
n = 3
#hanoitower(src,dest,mid,n)


def exp1(x,n):
    result = 1
    for i in range(n):
        result *= x
    return result

def exp2(x,n):
    if n ==0:
        return 1
    result = exp2(x**2,n/2) 
    if n%2 == 0:
        return result
    else:
        return result * x

x = 2
n = 10
##print exp1(x,n)
##print exp2(x,n)


def isPalindrome(string):
    if len(string) < 2:
        return True
    elif string[0] == string[-1]:
        return isPalindrome(string[1:len(string)-1])
    else:
        return False

##string = 'a'    
##print isPalindrome(string)
##string = 'ab'    
##print isPalindrome(string)
##string = 'aba'    
##print isPalindrome(string)
##string = 'ababa'    
##print isPalindrome(string)
##string = 'abba'    
##print isPalindrome(string)


def gcd(m,n):
    if n > m:
        n,m = m,n    
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n)

##m = 21
##n = 15
##print gcd(m,n)
##m = 21
##n = 28
##print gcd(m,n)
##m = 21
##n = 105
##print gcd(m,n)



    
