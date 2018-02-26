from pointerqueue import Queue
from node import Node
from lcrstree import Tree

def LevelOrder(T):
	n = T.root
	#print n.val
	if n == None:
		print "empty tree!"
		return
	Q = Queue()
	Q.ENQUEUE(n)
	while Q.front != None:
		#c is the current node positon
		c = Q.front
		print str(c.val) + ", ",
		if c.left != None:
			Q.ENQUEUE(c.left)
		if c.right != None:
			Q.ENQUEUE(c.right)
		Q.DEQUEUE()



t = Tree()
n = Node(10)

t.root = n

t.INSERT(2)
t.INSERT(15)
t.INSERT(3)
t.INSERT(6)




LevelOrder(t)