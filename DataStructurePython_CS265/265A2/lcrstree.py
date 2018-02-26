import time
from node import Node

class Tree:
	def __init__(self):
		self.root = None
		self.lev = None #this is level 
	
	def PARENT(n,self):
		return n.parent

	def LEFTMOST_CHILD(n,self):
		while True:
			if n.left == None:
				return n
			else:
				n.left

	def RIGHT_SIBLING(self, n):
		n = n.parent
		if n.right != None:
			return n.right
		else:
			return None

	def LABEL(n,self):
		return n.data

	def ROOT(self):
		return self.root

	def AddOne(self,x):
		n = Node(x)
		if self.root == None:
			self.root = n
		elif self.root.left == None:
			self.root.left = n
		elif self.root.right == None:
			self.root.right = n
		else:
			self.AddOne(x)
		return

	def INSERT(self,x):
		p = self.root
		while True:
			if (x < p.val) and (p.left == None):
				n = Node(x)
				p.left = n
				return
			elif (x > p.val) and (p.right == None):
				n = Node(x)
				p.right = n
				return
			elif x < p.val:
				p = p.left
			elif x > p.val:
				p = p.right

def AddLeft(n,x):
	i = Node(x)
	#i.val = x
	n.left = i
	i.parent = n

def AddRight(n,x):
	i = Node(x)
	#i.val = x
	n.right = i
	i.parent = n


def MAKENULL(T):
	T = Tree()
	return

####################

'''
t = Tree()
n = Node(10)
#n.val = 1
t.root = n

t.INSERT(2)
t.INSERT(15)
t.INSERT(3)
t.INSERT(6)

print t.root.left.right.right.val
'''

#ListByLevel(t)





