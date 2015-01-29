#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150120
#Chapter7: Stack Structures
#------------------------------------------
#Convert the infix expression to postfix using Stack based on linked list.

from llistStack import Stack

def infix2postifix(string):
    s = Stack()
    for token in string:
        #print token
        if token in "+-/*()":
            if token in '+-':
                if not s.isEmpty() and s.peek() in "+-":
                    op =  s.pop()
                    print op,
                elif not s.isEmpty() and s.peek() not in "+-":
                    s.push(token)
                else:
                    s.push(token)
                    
        else:
            print token,


s = "A + B - C"        
infix2postifix(s)
