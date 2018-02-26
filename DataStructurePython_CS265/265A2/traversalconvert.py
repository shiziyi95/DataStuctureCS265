
from lcrstree import Tree
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.left = None
        self.right = None
        self.parent = None

def Inorder(root):
    if root:
        # First recur on left child
        Inorder(root.left)
        # then print the data of node
        print(root.val),
        # now recur on right child
        Inorder(root.right)

def Postorder(root):
    if root:
        # First recur on left child
        Postorder(root.left)
        # the recur on right child
        Postorder(root.right)
        # now print the data of node
        print(root.val),
 
 
# A function to do postorder tree traversal
def Preorder(root,l):
 
    if root:
        # First print the data of node
        print(root.val)
 
        # Then recur on left child
        print 'l',
        Preorder(root.left,l+1)
        
 
        # Finally recur on right child
        print 'r',
        Preorder(root.right,l)
        


######
l=0
t = Tree()
root = Node(10)
t.root = root
t.INSERT(1)
t.INSERT(20)
t.INSERT(5)
t.INSERT(15)
t.INSERT(7)
t.INSERT(16)
t.INSERT(4)
print "Preorder: "
Preorder(root,l)
print ""
