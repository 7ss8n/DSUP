
class Stack:
    def __init__(self):
        self._theElements = list()

    def __len__(self):
        return len(self._theElements)

    def isEmpty(self):
        return len(self._theElements) == 0

    def peek(self):
        assert not self.isEmpty(),"The stack is empty."
        return self._theElements[-1]

    def pop(self):
        assert not self.isEmpty(),"The stack is empty."
        value = self._theElements.pop()
        return value

    def push(self,item):
        self._theElements.append(item)

    #for debug test
    def __str__(self):
        print "Stack is :",
        for elem in self._theElements:
            print elem,
        return ""
