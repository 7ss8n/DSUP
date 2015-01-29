#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter8: Advanced Linked List Structure
#------------------------------------------
#Implements the Double Linked List

class DListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



#test
head = DListNode(0)
tail = head

for i in range(1,10):
    temp = DListNode(i)
    tail.next = temp
    temp.prev = tail
    tail = temp
#print head.next
def PrintInorder(head):
    curNode = head
    while curNode is not None:
        print curNode.data
        curNode = curNode.next

#PrintInorder(head)

def PrintReverse(tail):
    curNode = tail
    while curNode is not None:
        print curNode.data
        curNode = curNode.prev
#PrintReverse(tail)


def searchUsingProb(head,tail,prob,target):
    if head is None:
        return False
    elif prob is None:
        prob = head

    if target < prob.data:
        while prob is not None and target <= prob.data:
            if target == prob.data:
                return True
            else:
                prob = prob.prev
    else:
        while prob is not None and target >= prob.data:
            if target == prob.data:
                return True
            else:
                prob = prob.next
    return False

target = -1
prob = None
#print searchUsingProb(head,tail,prob,target)

target = 0
#def delete(head,tail,target):
if head is None:
    print "the list in empty"
else:
    curNode = head
    while curNode is not None and curNode.data < target:
        curNode = curNode.next
    if curNode is not None and curNode.data == target:
        if curNode is head and curNode is tail:
            #print "1"
            head = curNode.next
            tail = head
        elif curNode is head:
            print "head 2"
            head.next.prev = None
            head = curNode.next
            print head.data
        elif curNode is tail:
            tail = curNode.prev
        else:
            curNode.prev.next = curNode.next
            curNode.next.prev = curNode.prev
    else: 
        print "the linked list doesn't have target."
            
        
#delete(head,tail,0)
PrintReverse(tail)
    
