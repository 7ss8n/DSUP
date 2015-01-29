from pylistStack import Stack

def isValidSource(srcfile):
    s = Stack()
    for line in srcfile:
        #print line
        for token in line:
            if token in "([{":
                s.push(token)
                print s
            elif token in ")]}":
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    print s
                    if (token == ")" and left != "(")or \
                       (token == "]" and left != "[")or \
                       (token == "}" and left != "{"):
                        return False
    return s.isEmpty()
                

#
srcfile = open('sum.c')
print isValidSource(srcfile)
