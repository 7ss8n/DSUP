#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20141229
#Chapter5 Searching and Sorting
'''
#-----------------------------
#List
t = range(1,11)
print t
key = 0
if key in t:
    print ("The key is in the array.")
else:
    print ("The key is not in the array.")


def linearsearch(theValues, target):
    n = len( theValues )
    for i in range( n ):
        #if the target is in the ith element,return True.
        if theValues[i] == target:
            return True
        
    return False
key1 = 0
key2 = 1
key3 = 10
print "#---linerasearch---#" 
print linearsearch(t, key1)
print linearsearch(t, key2)


def binarysearch( theValues, target ):
    low = 0
    high = len(theValues)-1
    
    while( low <= high ):
        mid = (low + high)/2
        if theValues[mid] == target:
            return True
        elif  target < theValues[mid]:
            high = mid - 1
        elif target > theValues[mid]:
            low = mid + 1
            
    return False
print "#---binarysearch---#"            
print binarysearch(t, key1)
print binarysearch(t, key2)
print binarysearch(t, key3)



##---------------------------
def sortedlinearsearch(theValues, target):
    n = len(theValues)
    for i in range( n ):
        #if the target is in the ith element,return True.
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False
        
print "#---sortedlinearsearch---#"            
print sortedlinearsearch(t, key1)
print sortedlinearsearch(t, key2)
print sortedlinearsearch(t, key3)

def findSmallest( theValues ):
    n = len(theValues)
    if n == 0:
        return 'empty'
    else:
        min = theValues[0]
    for i in range(n):
        if min > theValues[i]:
            min = theValues[i]
    return min

print "#---findSmallest---#"
t1 = range(10)
print t1
t2 = []
print t2
t3 = range(10,0,-1)
print t3
print findSmallest(t1)
print findSmallest(t2)
print findSmallest(t3)


def bubbleSorted( theValues ):
    n = len( theValues )
    for k in range(n-1):
        for i in range(n-1-k):
            if(theValues[i] > theValues[i+1]):
                temp = theValues[i+1]
                theValues[i+1] = theValues[i]
                theValues[i] = temp
#test
t1 = []
print 'before sorting',t1
bubbleSorted(t1)
print 'after sorting',t1
t2 = range(10)

print 'before sorting',t2
bubbleSorted(t2)
print 'after sorting',t2
t3 = range(10,0,-1)

print 'before sorting',t3
bubbleSorted(t3)
print 'after sorting',t3

t4 = [10,51,2,18,4,31,13,5,23,64,29]
print 'before sorting',t4
bubbleSorted(t4)
print 'after sorting',t4




def selectionSorted( theValues ):
    n = len( theValues )    
    for k in range( n ):
        #print 'k = ',k
        min = k        
        for i in range(k+1,n):
            #print 'i = ',i
            if(theValues[i] < theValues[min]):
                min = i
        if k!=min:
            temp = theValues[k]
            theValues[k] = theValues[min]
            theValues[min] = temp
            #print 'theValues = ',theValues
#test
t1 = []
print 'before sorting',t1
selectionSorted(t1)
print 'after sorting',t1
t2 = range(10)

print 'before sorting',t2
selectionSorted(t2)
print 'after sorting',t2

t3 = range(10,0,-1)
print 'before sorting',t3
selectionSorted(t3)
print 'after sorting',t3

t4 = [10,51,2,18,4,31,13,5,23,64,29]
print 'before sorting',t4
selectionSorted(t4)
print 'after sorting',t4                
'''

def insertionSorted( theValues ):
    n = len( theValues )    
    for i in range( 1, n ):
        #print 'i = ',i
        for j in range(i,0,-1):
            #print 'j = ',j
            if theValues[j] < theValues[j-1]:
                temp = theValues[j]
                theValues[j] = theValues[j-1]
                theValues[j-1] = temp
                #print 'theValues = ',theValues 

#test
t1 = []
print 'before sorting',t1
insertionSorted(t1)
print 'after sorting',t1
t2 = range(10)

print 'before sorting',t2
insertionSorted(t2)
print 'after sorting',t2

t3 = range(10,0,-1)
print 'before sorting',t3
insertionSorted(t3)
print 'after sorting',t3

t4 = [10,51,2,18,4,31,13,5,23,64,29]
print 'before sorting',t4
insertionSorted(t4)
print 'after sorting',t4 
