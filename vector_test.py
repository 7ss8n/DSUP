#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150101
#Chapter2: Programing Projects2.1, Vector ADT using Array class.
#Test module
#------------------------------------------

from vector import Vector
Vect = Vector()
print Vect
##for i in range(64):
##    print 'before append len = ',len(Vect)
##    Vect.append(i)
##    print "Vect[{}] = ".format(i),Vect[i]
##    print 'after append len = ',len(Vect)

def print_vector(Vect):
    for i in range(len(Vect)):
        print Vect[i],
    print ""

for i in range(8):
    print 'before append len = ',len(Vect)
    Vect.insert(0,i)
    #print "Vect[{}] = ".format(0),Vect[0]
    print_vector(Vect)
    print 'after append len = ',len(Vect)
    print ""
