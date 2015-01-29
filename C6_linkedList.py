#C6 Linked Structures

class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

def traversal(head):
    curNode = head
    while curNode is not None:
        print curNode.data,
        curNode = curNode.next
    print""

def unorderedSearch(head,target):
    curNode = head
    while curNode is not None and curNode.data != target :
        curNode = curNode.next
    return curNode != None

def addItem(head,value):
    newNode = ListNode(value)
    newNode.next = head
    head = newNode
    return head

def removeItem(head,target):
    preNode = None
    curNode = head
    while curNode is not None and curNode.data !=target:
        preNode = curNode
        curNode = curNode.next
        
    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            preNode.next = curNode.next
    return head

a = ListNode(11)

#b = ListNode(52)
#c = ListNode(18)
a.next = ListNode(52)
a.next.next = ListNode(18)

traversal(a)
print unorderedSearch(a,52)
print unorderedSearch(a,2)

a = addItem(a,7)
traversal(a)
print unorderedSearch(a,7)

a= removeItem(a,7)
traversal(a)

a= removeItem(a,19)
traversal(a)
