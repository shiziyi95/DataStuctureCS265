from node import Node

import time
class Node:
	def __init__(self, x):
 		self.val = x
		self.next = None

class LinkedList:
	def __init__( self ):
		self.head = None
		
	
	def ADDONE(self, x):
		n = Node(x)
		if self.head == None:
			self.head = n
			return
		p = self.head
		while p.next != None:
			p = p.next 
		p.next = n
		return

	def FIRST(self):
		return self.head

	def END(self):
		tmp = self.FIRST()
		while True:
			tmp = tmp.next
			if tmp.next == None:
				return tmp

	def RETRIVE(self, p):
		tmp = self.head
		for i in range(0, p):
			tmp = tmp.next
		return tmp

	def LOCATE(self, x):
		tmp = self.FIRST()
		c = 0
		while True:
			tmp = tmp.next
			c = c + 1
			if tmp.val == x:
				return tmp

	def NEXT(self, n):
		return n.next

	def PREVIOUS(self, n):
		tmp = self.FIRST()
		while True:
			tmp = tmp.next
			if tmp.next == n:
				return tmp

	def INSERT(self, p, x):
		n = Node()
		n.val = x #creat node with val x
		if p ==0:
			n.next = self.head
			self.head = n
		else:
			tmp = self.FIRST()
			for i in range(0, p-1):
				if tmp.next != None:
					tmp = tmp.next #reach the desinted location
			n.next = tmp.next
			tmp.next = n
		return

	def DELETE(self, p):
		target = self.FIRST()
		prev = self.FIRST()
		if p == 0:
			self.head = target.next
		else:
			for i in range(0, p-1):
					target = target.next
			for i in range(0, p-2):
					prev = prev.next
		if target.next != None:
			prev.next = target.next
		else:
			prev.next = None
		return

	def MAKENULL(self):
		self = LinkedList()
		self.head = None
		return LinkedList()
	def printList(self):
		n = self.head
		i = 0
		while n :
			i += 1
			print str(i) + "th: " + str(n.val)
			n = n.next
###############
def mergetwo(a,b):
	if (isinstance(a, LinkedList)) and (isinstance(b, LinkedList)):
		a.END().next = b.head
		return a
	elif (isinstance(a, int)) and (isinstance(b, LinkedList)):
		a.next = b.head
	elif (isinstance(a, int)) and (isinstance(b, LinkedList)):
		return

def isLinear(L):
	p = L.head
	while True:
		#print p.val
		p = p.next
		
		if isinstance(p.val, int) == False:
			return False
		if p.next == None:
			return True

def listconcat(L):
	while isLinear(L) == False:
		p = L.head
		b = L.head #p is one space infront of b
		p = p.next
		while True: 
			if p.next == None:
				return
			if isinstance(p.val, int) == False:
				b.next = p.val.head
				p.val.END().next = p.next
			p = p.next
			b = b.next

a = LinkedList()
for i in range(5):
	a.ADDONE(i+1)

b = LinkedList()
for i in range(3):
	b.ADDONE(i+1)

c = LinkedList()
for i in range(3):
	b.ADDONE(i+1)
'''
a.printList()
print ""
b.printList()
print ''
c = LinkedList()
c = mergetwo(a,b)
c.printList()
'''
#print isinstance(c.head.val, int)
megaL = LinkedList()
megaL.ADDONE(1)
megaL.ADDONE(2)
megaL.ADDONE(a)
megaL.ADDONE(b)
megaL.ADDONE(a)
megaL.ADDONE(c)
#print isLinear(megaL)
listconcat(megaL)
megaL.printList()
'''
Tril = LinkedList()
Tril.ADDONE(1)
Tril.ADDONE(megaL)
Tril.ADDONE(a)
listconcat(Tril)
'''