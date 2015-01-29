#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150127
#Chapter1: ADT
#Programming Projects
###1.1 A click counter is a small hand-held device that contains a push button and
###a count display. To increment the counter, the button is pushed and the new
###count shows in the display. Clicker counters also contain a button that can be
###pressed to reset the counter to zero. Design and implement the Counter ADT
###that functions as a hand-held clicker.
#------------------------------------------
#Implements the Counter ADT.

class Counter:
    def __init__(self):
        self._count = 0

    def push(self):
        self._count += 1
        print "Count :",self._count

    def reset(self):
        self._count = 0
        print "Reset Counter to zero."


#------------------------------------------
#test Counter ADT.
#testcase

def main():
    c = Counter()
    for i in range(30):
        if i%2 ==0:
            c.push()
        elif i%13 == 0:
            c.reset()

main()
