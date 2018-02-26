import traversalconvert
from node import Node
from lcrstree import Tree

t = Tree()
root = Node(10)
t.root = root
t.INSERT(1)
t.INSERT(20)
t.INSERT(5)
t.INSERT(15)
t.INSERT(7)
print "Preorder: "
Preorder(root)
print ""

print "Inorder: "
Inorder(root)
print ""

print "Postorder: "
Postorder(root)
print ""