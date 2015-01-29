#------------------------------------------
#Book:Data Structures and Algorithms Using Python
#Author:zhuyoujun
#Date:20150118
#Chapter13: Binary Tree Structures
#------------------------------------------
#Implements the Binary Tree ADT.

# The storage class for creating binary tree nodes.
class _BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    
def PreorderTraversal(subtree):
    if subtree == None:
        #print ""
        return
    else:
        print subtree.data
        PreorderTraversal(subtree.left)
        PreorderTraversal(subtree.right)
    

def InorderTraversal(subtree):
    if subtree == None:
        #print ""
        return
    else:        
        InorderTraversal(subtree.left)
        print subtree.data
        InorderTraversal(subtree.right)

def PostorderTraversal(subtree):
    if subtree == None:
        #print ""
        return
    else:        
        PostorderTraversal(subtree.left)
        PostorderTraversal(subtree.right)
        print subtree.data

##def search(subtree,value):
##    if subtree != None :
##        if subtree.data == value:
##            print "0subtree.data",subtree.data
##            return True
##        else:
##            print "1subtree.data",subtree.data
##            search(subtree.left,value)
##            #print ""
##            search(subtree.right,value)
##            #print ""
##            return False

from  pylistQueue import Queue   
def breadFirstTraversal(subtree):
    q = Queue()
    q.enqueue(subtree)
    while not q.isEmpty():
        t= q.dequeue()
        if t.left:
            q.enqueue(t.left)
        if t.right:
            q.enqueue(t.right)
        print t.data
        

def sizeOfTree(subtree):
    if subtree is None:
        return 0
    else:
        return 1 + sizeOfTree(subtree.left)\
                + sizeOfTree(subtree.right)

def depthOfTree(subtree):
    if subtree is None:
        return 0
##    elif subtree.left is None and subtree.right is None:
##        return 1
    else:
        return 1 + max(depthOfTree(subtree.left),depthOfTree(subtree.right))
        
def sameTree(tree1,tree2):
    if tree1 is None and tree2 is None:
        return True
    elif tree1 is not None and tree2 is not None:
        if tree1.data == tree2.data and \
           sameTree(tree1.left,tree2.left) and \
           sameTree(tree1.right,tree2.right):
            return True
        else:
            return False
    else:
        return False
    
def mirrorTree(subtree):
    if subtree is None:
        return
    else:
        mirrorTree(subtree.left)
        mirrorTree(subtree.right)
        temp = subtree.left
        subtree.left = subtree.right
        subtree.right = temp

####
def printList(lst,n):
    for i in range(n):
        print lst[i],"->",
    print ""

def root2LeafPathRecur(subtree,lst,n):
    if subtree is None:
        return
    lst[n] = subtree.data
    n += 1
    if subtree.left is None and subtree.right is None:
        printList(lst,n)
        
    else:
        root2LeafPathRecur(subtree.left,lst,n)
        root2LeafPathRecur(subtree.right,lst,n)

def root2LeafPath(subtree):
    lst = 100*[None]
    root2LeafPathRecur(subtree,lst,0)
####

def numberOfLeaves(subtree):
    if subtree is None:
        return 0
    elif subtree.left is None and subtree.right is None:
        return 1
    else:
        return numberOfLeaves(subtree.left) + numberOfLeaves(subtree.right)



    
def main():
    root = _BinaryTreeNode("T")
    X = _BinaryTreeNode("X")
    C = _BinaryTreeNode("C")
    root.left = X
    root.right = C
    B = _BinaryTreeNode("B")
    G = _BinaryTreeNode("G")
    X.left = B
    X.right = G
    Z = _BinaryTreeNode("Z")
    G.left = Z
    J = _BinaryTreeNode("J")
    R = _BinaryTreeNode("R")
    C.left = J
    C.right = R
    K = _BinaryTreeNode("K")
    M = _BinaryTreeNode("M")
    R.left = K
    R.right = M

    root1 = _BinaryTreeNode("G")
    root1.left = X
    root1.right = C    

##    print "PreorderTraversal"
##    PreorderTraversal(root)
##    
##    print "InorderTraversal"    
##    InorderTraversal(root)
##
##    print "PostorderTraversal"     
##    PostorderTraversal(root)

####    data = "T"
####    print "{0} is in tree?{1}".format(data,search(root,data))
####    
####    data = "Z"
####    print "{0} is in tree?{1}".format(data,search(root,data))
####
####    data = "M"
####    print "{0} is in tree?{1}".format(data,search(root,data))
####
####    data = "S"
####    print "{0} is in tree?{1}".format(data,search(root,data))

##    print "breadFirstTraversal"
##    breadFirstTraversal(root)
##    print "size of the tree: ",sizeOfTree(root)
##    print "is the same Tree?",sameTree(root,root1)
##    print "depth of the tree root: 4?",depthOfTree(root)
##    print "depth of the tree X: 3?",depthOfTree(X)
##    print "depth of the tree J: 1?",depthOfTree(J)
##    print "depth of the tree R: 2?",depthOfTree(R)
##    print "depth of the tree K: 1?",depthOfTree(K)
##    
##    print "InorderTraversal"    
##    InorderTraversal(root) 
##    mirrorTree(root)
##    print "InorderTraversal"    
##    InorderTraversal(root)

##    root2LeafPath(root)

    print "number of leaves in Tree {} is 5?{}".format(root.data,numberOfLeaves(root))
    print "number of leaves in Tree {} is 2?{}".format(X.data,numberOfLeaves(X))    
    print "number of leaves in Tree {} is 1?{}".format(J.data,numberOfLeaves(J))
    print "number of leaves in Tree {} is 3?{}".format(C.data,numberOfLeaves(C))
    
#call
main()
