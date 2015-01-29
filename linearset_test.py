#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150102
#Chapter3: Set ADT Test module
#------------------------------------------
#Testing the Set ADT 
from linearset import Set

def linearset_test():
    # test init function
    s1 = Set()
    s2 = Set()
    s3 = Set()
    # test len function

    for i in range(16):
        s1.add(i)
    print 'len = ',len(s1)
    print"s1:"
    for elem in s1:
        print elem,
    print ""

    for i in range(16):
        s2.add(i)
    print 'len = ',len(s2)
    print"s2:"
    for elem in s2:
        print elem,
    print ""
    print"s2: using print function"
    print s2
    
    for i in range(0,32,2):
        s3.add(i)
    print 'len = ',len(s3)
    print"s3:"
    for elem in s3:
        print elem,
    print ""
    
    print "s1 == s2",s1 == s2
    print "s1 == s3",s1 == s3

    print "s3 is the SubsetOf s2 ?shuould be False:  ",s3.isSubsetOf(s2)
    print "s2 is the SubsetOf s1 ?shuould be True:  ",s2.isSubsetOf(s1)
    print "s2 is the isProperSubsetOf s1 ?shuould be False:  ",s2.isProperSubsetOf(s1)
    
    s4 = s1.union(s3)
    print"s4 is the union of s1 and s3"
    for elem in s4:
        print elem,
    print ""
    
    s5 = s1.intersect(s3)   
    print"s5 is the intersect of s1 and s3"
    for elem in s5:
        print elem,
    print ""
    
    s6 = s1.difference(s3)   
    print"s6 is the difference of s1 and s3"
    for elem in s6:
        print elem,
    print ""

    s7 = s1 + s3
    print"s7 is the union of s1 and s3,using add "
    for elem in s7:
        print elem,
    print ""
    
    s8 = s1 * s3  
    print"s8 is the intersect of s1 and s3,using mul"
    for elem in s8:
        print elem,
    print ""
        
    s9 = s1 - s3 
    print"s9 is the difference of s1 and s3,using sub"
    for elem in s9:
        print elem,
    print ""

    # test 
    s10 = Set(1,2,3)
    print"s10 test init"
    for elem in s10:
        print elem,
    print ""
    
    print"s10 : test _str"
    s10._str()

    print s10
    
    
# call         
#linearset_test()


def linearset_examples():
    smith = Set()
    smith.add("CSCI-112")
    smith.add("MATH-121")
    smith.add("HIST-340")
    smith.add("ECON-101")    

    roberts = Set()
    roberts.add("POL-101")
    roberts.add("ANTH-230")
    roberts.add("CSCI-112")
    roberts.add("ECON-101")

    if(smith ==roberts ):
        print "Smith and Roberts are taking the same courses"
    else:
        sameCoures = smith.intersect( roberts )
        if sameCoures.isEmpty():
            print "Smith and Roberts are not taking the same courses."
        else:
            print "Smith and Roberts are  taking some same courses."
            print sameCoures
        uniqueCourses = smith.difference( roberts )
        print "Smith are  taking some different courses compared to Roberts."
        print uniqueCourses
        
#call
linearset_examples()
