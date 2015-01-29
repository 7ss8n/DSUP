#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150120
#Chapter7: Stack Structures
#------------------------------------------
#Implements the Postfix Calculator ADT using Stack based on linked list

from llistStack import Stack
from math import sqrt,sin,cos,tan

class PostfixCalculator:
    def __init__(self):
        self._operandStack = Stack()
        self._saveStack = Stack()

    def value(self,x):
        #print "x = ",x
        self._operandStack.push(int(x))

    def result(self):
        if not self._operandStack.isEmpty():
            return self._operandStack.peek()

    def clear(self):
        while not self._operandStack.isEmpty:
            self._operandStack.pop()

    def clearLast(self):
        if not self._operandStack.isEmpty:
            self._operandStack.pop()

    def store(self):
        if not self._operandStack.isEmpty:
            value = self._operandStack.pop()
            self._saveStack.push(value)
        
    def recall(self):
        if not self._saveStack.isEmpty:
            value = self._saveStack.pop()
            self._operandStack.push(value)

    def compute(self,op):
        if op in "+-/**":
            if not self._operandStack.isEmpty():
                op2 = self._operandStack.pop()
            if not self._operandStack.isEmpty():
                op1 = self._operandStack.pop()

            if op == '+':
                result = op1 + op2
            elif op == '-':
                result = op1 - op2
            elif op == '/':
                result = op1 / op2
            elif op == '*':
                result = op1 * op2
            elif op == '**':
                result = op1**op2
            
        elif op in ["abs","sqrt","sin","cos","tan"]:
            if not self._operandStack.isEmpty():
                op1 = self._operandStack.pop()

            if op == "abs":
                result = abs(op1)
            elif op == "sqrt":
                result = sqrt(op1)
            elif op == "sin":
                result = sin(op1)
            elif op == "cos":
                result = cos(op1)                
            elif op == "tan":
                result = tan(op1)        
        
        #print "result = ",result
        self._operandStack.push(result)


#test
'''
string = "1 2 + 3 * 4 2 / - 2 ** 100 -"
string = string.split()

cal = PostfixCalculator()
i = 0
while i <len(string):
    if string[i] in "+-/**":
        cal.compute(string[i])
        i += 1
    else:
        cal.value(string[i])
        i += 1
print cal.result()


cal.clear()
string = "-1 abs sqrt sin cos"
string = string.split()
i = 0
while i <len(string):
    if string[i] in ["abs","sqrt","sin","cos","tan"]:
        cal.compute(string[i])
        i += 1
    else:
        cal.value(string[i])
        i += 1
print cal.result()
'''

def postfixCalculator():
    opertor = {"ADD":"+","SUB":"-","MUL":"*","DIV":"/","POW":"**"}
    cal = PostfixCalculator()
    string = raw_input("")
    string = string.split()
    while string[0]!="RESULT":
                
        if string[0] == "CLR":
            cal.clear()
        elif string[0] == "CLRLAST":
            cal.clearLast()
        elif string[0] == "ENTER":
            cal.value(string[1])
        elif string[0] in opertor:
             cal.compute(opertor[string[0]])
        string = raw_input("")
        string = string.split()
    if string[0]=="RESULT":
        print "result: ",cal.result()
        
            
postfixCalculator()

