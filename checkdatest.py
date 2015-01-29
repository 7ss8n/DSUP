#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20141229
#Chapter1 ADT

#------------------------------------------
#Extracts a collection of birth dates from the user and determines
#if each individaul is at least 21 years of age.

from date import Date
def main():
    #Prompts for and extracts the Gregorian date components.
    #Returns a Date object or None when the user has finished entering dates.
    def promptExtractDate():
        print("Enter a birth date.")
        month = int(raw_input("month(0 to quit:) "))
        if month == 0:
            return None
        else:
            day = int(raw_input("day: "))
            year = int(raw_input("year: "))
            return Date(month,day,year)

    #Date before which a person must have born to be 21 or older.
    bornBefore = Date(6,1,1988)

    #Extrate birth dates from user and determine if 21 or older.
    date = promptExtractDate()
    while date is not None:
        if date <= bornBefore:
            print "Is at least 21 years of age:",date
        date = promptExtractDate()



#Call the main routine.
main()
