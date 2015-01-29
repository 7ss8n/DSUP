#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150102
#Chapter3: Map ADT test module
#------------------------------------------
#Test module of the Map ADT using a list
from linearmap import Map

def linearmap_test():
    #test init function
    M1 = Map()
    #test length function
    print len(M1)
    
    for k in range(16):
        v = chr(k+65)
        #test add funct
        M1.add(k,v)
        print len(M1)
    #test valueOf() func
    for k in range(16):
        print'value of {} is '.format(k), M1.valueOf(k)
    #print M1.valueOf(16)

    #test in
    for k in range(17):
        if k  in M1:
            print '{} is in the Map'.format(k)
        else:
            print '{} is not the Map'.format(k)
    # test keyArray func
    keyArr = M1.keyArray()
    print "keyArray"
    for i in range(len(keyArr)):
        print keyArr[i]
    

    #print M1._entryList
    print "test remove funct"
    for k in range(16):
        #test remove funct
        M1.remove(k)
        print len(M1)


#call
linearmap_test()   
