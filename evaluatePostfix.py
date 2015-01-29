from pylistStack import Stack

def evaluatePostfix(expr):
    s = Stack()
    expr = expr.split()
    #print expr
    for elem in expr:
        #print 'elem = ',elem
        if elem in "+":
            if s.isEmpty():
                return False
            else:
                op1 = int(s.pop())
                if s.isEmpty():
                    return False
                op2 = int(s.pop())
                op = op2 + op1
                #print op
                s.push(op)
        elif elem in "-":
            if s.isEmpty():
                return False
            else:
                op1 = int(s.pop())
                if s.isEmpty():
                    return False
                op2 = int(s.pop())
                op = op2 - op1
                s.push(op)
        elif elem in "*":
            if s.isEmpty():
                return False
            else:
                op1 = int(s.pop())
                if s.isEmpty():
                    return False
                op2 = int(s.pop())
                op = op2 * op1
                s.push(op)
        elif elem in "/":
            if s.isEmpty():
                return False
            else:
                op1 = int(s.pop())
                if s.isEmpty():
                    return False
                op2 = int(s.pop())
                op = op2 / op1
                s.push(op)
        else:
            s.push(elem)
            #print s.peek()

    result = s.pop()
    #print "result = ",result
    if not s.isEmpty():
        return "Invalid experssion"
    else:
        return result

expr = "10 5 +"
print evaluatePostfix(expr)
assert evaluatePostfix(expr) == 15,"error!"

expr = "10 5 -"
print evaluatePostfix(expr)
assert evaluatePostfix(expr) == 5,"error!"

expr = "10 5 - 5 *"
print evaluatePostfix(expr)
assert evaluatePostfix(expr) == 25,"error!"

expr ="8 2 3 + * 4 /"
print evaluatePostfix(expr)
assert evaluatePostfix(expr) == 10,"error!"

expr ="8 2 * 3 4 +"
print evaluatePostfix(expr)
assert evaluatePostfix(expr) == 'Invalid experssion',"error!"
