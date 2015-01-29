#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150127
#Chapter1: ADT
#Programming Projects
####1.6 We can use a Time ADT to represent the time of day, for any 24-hour period,
####as the number of seconds that have elapsed since midnight. Given the following
####list of operations, implement the Time ADT.
####   >>Time( hours, minutes, seconds ): Creates a new Time instance and ini-
####    tializes it with the given time.
####   >>hour(): Returns the hour part of the time.
####   >>minutes(): Returns the minutes part of the time.
####   >>seconds(): Returns the seconds part of the time.
####   >>numSeconds( otherTime ): Returns the number of seconds as a positive
####    integer between this time and the otherTime.
####   >>isAM(): Determines if this time is ante meridiem or before midday (at or
####    before 12 o'clock noon).
####   >>isPM(): Determines if this time is post meridiem or after midday (after
####    12 o'clock noon).
####   >>comparable ( otherTime ): Compares this time to the otherTime to de-
####    termine their logical ordering. This comparison can be done using any of
####    the Python logical operators.
####   >>toString (): Returns a string representing the time in the 12-hour format
####hh:mm:ss. Invoked by calling Python's str() constructor.
#------------------------------------------
#Implements the Time ADT.

class Time:
    #Construct the time by given hours,minutes,seconds
    def __init__(self,hours,minutes,seconds):
        self._hours   = hours
        self._minutes = minutes
        self._seconds = seconds
        self._totalSeconds = hours*3600 + minutes*60 + seconds
        
    #Return the hour part of the time
    def hours(self):
        return self._hours
    
    #Return the minute part of the time
    def minutes(self):
        return self._minutes

    #Return the minute part of the time
    def seconds(self):
        return self._seconds
    

    #Return the absolute difference between self and otherTime
    def numSeconds(self,otherTime):
        if self._totalSeconds < otherTime._totalSeconds:
            return otherTime._totalSeconds - self._totalSeconds
        else:
            return self._totalSeconds - otherTime._totalSeconds

    #Judge if the time is AM or not.
    def isAM(self):
        if (self._hours < 12) or (self._hours == 12 and self._minutes == 0 and self._seconds == 0):
            return True
        else:
            return False

    #Judge if the time is PM or not.
    def isPM(self):
        if (self._hours > 12) or (self._hours == 12 and (self._minutes != 0 and self._seconds != 0)):
            return True
        else:
            return False
    #Judge self and otherTime is equal or not.
    def __eq__(self,otherTime):
        return  self._totalSeconds == otherTime._totalSeconds

    #Judge self is less than otherTime or not.
    def __lt__(self,otherTime):
        return  self._totalSeconds < otherTime._totalSeconds

    #Judge self is greater than otherTime or not.
    def __gt__(self,otherTime):
        return  self._totalSeconds > otherTime._totalSeconds

    #Returns a string representing the time in the 12-hour format: hh:mm:ss
    def __str__(self):
        if self.isPM() :
            return  "%02d:%02d:%02dPM" % (self._hours%12, self._minutes, self._seconds)
        else:
            return  "%02d:%02d:%02dAM" % (self._hours, self._minutes, self._seconds)

#------------------------------------------
#test Counter ADT.
#testcase

def main():
    t0 = Time(0,0,0)
    t1 = Time(11,59,59)    
    t2 = Time(12,0,0)
    t3 = Time(13,59,59)
    t4 = Time(23,59,59)
    print "t0 = ",t0    
    print "t1 = ",t1
    print "t2 = ",t2    
    print "t3 = ",t3
    print "t4 = ",t4

    print "t1({0})'s hours:?{1}".format(t1,t1.hours())
    print "t1({0})'s minutes:?{1}".format(t1,t1.minutes())
    print "t1({0})'s seconds:?{1}".format(t1,t1.seconds())
    print "Is the diffrence seconds between t1({0}) and t2({1})?{2}".format(t1,t2,t1.numSeconds(t2))    
    print "Is t1({0}) < t2({1})?{2}".format(t1,t2,t1<t2)
    print "Is t1({0}) == t2({1})?{2}".format(t1,t2,t1==t2)
    print "Is t1({0}) > t2({1})?{2}".format(t1,t2,t1>t2)
    print "Is t1({0}) AM?{1}".format(t1,t1.isAM())    
    print "Is t2({0}) AM?{1}".format(t2,t2.isAM())
    print "Is t3({0}) AM?{1}".format(t3,t3.isAM())

    print "Is t1({0}) PM?{1}".format(t1,t1.isPM())    
    print "Is t2({0}) PM?{1}".format(t2,t2.isPM())
    print "Is t3({0}) PM?{1}".format(t3,t3.isPM())
    
main()
