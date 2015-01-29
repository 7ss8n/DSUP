#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150129
#Chapter1: ADT
#------------------------------------------
#Implements the Student Record Report form data extracted from an external source.
from studentfile import StudentFileReader

FILE_NAME  = "student.txt"

def main():
    student = StudentFileReader(FILE_NAME)
    student.open()
    studentList = student.fetchAll()
    student.close()

    studentList.sort(key = lambda rec:rec.idNum)

    printReport(studentList)

def printReport(theList):
    # The class names associated with the class codes.
    classNames = ( None, "Freshman", "Sophomore", "Junior", "Senior" )

    # Print the header.
    print( "LIST OF STUDENTS".center(50) )
    print( "" )
    print( "%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA' ) )
    print( "%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))
    
    # Print the body.
    for record in theList :
        print( "%5d %-25s %-10s %4.2f" % \
               (record.idNum, \
                record.lastName + ', ' + record.firstName,
                classNames[record.classCode], record.gpa) )
    
    # Add a footer.
    print( "-" * 50 )
    print( "Number of students:", len(theList) )

#Call the main()
main()
