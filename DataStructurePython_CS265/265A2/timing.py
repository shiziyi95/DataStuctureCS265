from traversalconvert import Inorder
from traversalconvert import Postorder
from traversalconvert import Preorder
from node import Node
from lcrstree import Tree
import random
import time

t = Tree()
root = Node(50)
t.root = root
for i in random.sample(xrange(1,100), 50):
	if i == 50:
		continue
	t.INSERT(i)
	'''
t.INSERT(1)
t.INSERT(20)
t.INSERT(5)
t.INSERT(15)
t.INSERT(7)
t.INSERT(8)
'''
print "Preorder: "
start = time.time()
Preorder(root)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "\nTime taken to insertFront list is " + timeTaken + " milliseconds"
print s
print ""

print "Inorder: "
start = time.time()
Inorder(root)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "\nTime taken to insertFront list is " + timeTaken + " milliseconds"
print s
print ""

print "Posrorder: "
start = time.time()
Postorder(root)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "\nTime taken to insertFront list is " + timeTaken + " milliseconds"
print s
print ""



