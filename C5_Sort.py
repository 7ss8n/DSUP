#Date:2015/1/11
#------------------------------------------------
def bubbleSorted(theValues):
    for index in range(len(theValues)):
        for k in range(len(theValues)-1-index):
            if theValues[k]>theValues[k+1]:
                theValues[k],theValues[k+1] = theValues[k+1],theValues[k]
                
#------------------------------------------------
def bubbleSorted_Improved(theValues):
    for index in range(len(theValues)):
        sortedFlag = 0
        print "index = ",index
        for k in range(len(theValues)-1-index):
            print "k = ",k
            if theValues[k]>theValues[k+1]:
                theValues[k],theValues[k+1] = theValues[k+1],theValues[k]
                sortedFlag = 1
            print theValues
        if sortedFlag == 0:
            return
        
def bubbleSorted_test():
    #test bubbleSorted
    print 'bubbleSorted'
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

#call the test
#bubbleSorted_test()

def bubbleSorted_Improved_test():
    #test bubbleSorted_Improved
    print 'bubbleSorted_Improved'
    t1 = []
    print 'before sorting',t1
    bubbleSorted_Improved(t1)
    print 'after sorting',t1
    
    t2 = range(10)
    print 'before sorting',t2
    bubbleSorted_Improved(t2)
    print 'after sorting',t2
    
    t3 = range(10,0,-1)
    print 'before sorting',t3
    bubbleSorted_Improved(t3)
    print 'after sorting',t3

    t4 = [10,51,2,18,4,31,13,5,23,64,29]
    print 'before sorting',t4
    bubbleSorted_Improved(t4)
    print 'after sorting',t4

####call the test
#bubbleSorted_Improved_test()
    
#------------------------------------------------
def selectionSorted(theValues):    
    for index in range(len(theValues)-1):
        #print "index = ",index
        small = index
        for k in range(index+1,len(theValues)):
            #print "k = ",k
            if theValues[k]<theValues[small]:
                small = k
        #print "small = ",small
        if small != index:
            theValues[index],theValues[small] = theValues[small],theValues[index] 
        #print "theValues = ",theValues
        
def selectionSorted_test():
    #test
    print 'selectionSorted'
    
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

####call the test
#selectionSorted_test()

#------------------------------------------------
def insertionSorted(theValues):    
    for index in range(1,len(theValues)):
        print 'index = ',index
        for k in range(index,0,-1):
            print 'k = ',k
            if theValues[k]<theValues[k-1]:
                theValues[k],theValues[k-1] = theValues[k-1],theValues[k]
                print "theValues = ",theValues
            else:
                print "theValues = ",theValues
                break
            

def insertionSorted_test():
    #test
    print 'insertionSorted'
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

#call the test
insertionSorted_test()
