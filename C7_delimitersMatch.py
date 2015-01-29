#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150120
#Chapter7: Stack Structures
#------------------------------------------
#Implements the delimiter match algorithm using Stack ADT based on linked list.
#the delimiter set is "(),[],{},<>"
from llistStack import Stack

def delimiterMatch(srcfile):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token in "([{<":
                s.push(token)
            elif token in ")]}>":
                if s.isEmpty():
                    return False
                else:
                    left  = s.pop()
                    if (token == ')' and left != '(') or \
                       (token == ']' and left != '[') or \
                       (token == '}' and left != '{') or \
                       (token == '>' and left != '<'):
                        return False        
    return True


##srcfile = open('delimeterMatch_test.c')
##print delimiterMatch(srcfile)
##srcfile.close()

def skip_commentsOfcpp(srcfile):
    fid = open(srcfile,'w')
    for line in srcfile:
        temp = ''
        for token in line:
            if token == '/' and temp =='/':
                break
            elif tolen == '/' and temp == '':
                temp = '/'
            

def delimiterMatchAddComments(srcfile):
    s = Stack()
    for line in srcfile:
        temp = ""
        for token in line:
            if token in "([{":
                s.push(token)
                #print s
            elif token in ")]}":
                if s.isEmpty():
                    #print "1"
                    return False
                else:
                    #print s
                    left  = s.pop()
                    #print s
                    if (token == ')' and left != '(') or \
                       (token == ']' and left != '[') or \
                       (token == '}' and left != '{') :
                       #(token == '>' and left != '<'):
                        #print "2"
                        return False
            elif token == '/' and temp =='/':
                break
            elif token == '/' and temp == '':
                temp = '/'
            
    return True


srcfile = open('sum.c')
print delimiterMatchAddComments(srcfile)
srcfile.close()
