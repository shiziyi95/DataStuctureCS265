import time
class Node:
	def __init__( self ):
 		self.val = None
		self.next = None

class LinkedList:
	def __init__( self ):
		self.head = None
		self.tail = None
		
	
	def ADDONE(self, x):
		n = Node()
		n.val = x

		if self.head == None:
			self.head = n

		if self.tail != None:
			self.tail.next = n

		self.tail = n
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
#####
def insertFront(L):
	L.MAKENULL()
	L.INSERT(0,7)

def insertBack(L):
	L.MAKENULL()
	tmp = L.FIRST()
	i = 1
	while tmp.next != None:
		i = i + 1
		tmp = tmp.next
	L.INSERT(i,8)

def make64(L):
	L.MAKENULL()
	for i in range(64):
		L.INSERT(0,i)

def trav(L):
	L.MAKENULL()
	tmp = L.FIRST()
	while tmp.next != None:
		tmp = tmp.next

def iterateDeleteFront(L):
	L.MAKENULL()
	tmp = L.FIRST()
	i = 1
	while tmp.next != None:
		i = i + 1
		tmp = tmp.next
	for x in range(i):
		L.DELETE(0)

def iterateDeleteBack(L):
	L.MAKENULL()
	tmp = L.FIRST()
	i = 1
	while tmp.next != None:
		i = i + 1
		tmp = tmp.next
	for x in range(i,-1, -1):
		L.DELETE(x)
############
a = LinkedList()


print "welcome to counting pinterList: list size - 64\n"
start = time.time()
insertFront(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to insertFront list is " + timeTaken + " milliseconds"
print s

print ""
start = time.time()
insertBack(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to insertBack list is " + timeTaken + " milliseconds"
print s

make64(a)
print ""
start = time.time()
iterateDeleteFront(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to iterateDelteFront list is " + timeTaken + " milliseconds"
print s

make64(a)
print ""
start = time.time()
iterateDeleteBack(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to iterateDelteBack list is " + timeTaken + " milliseconds"
print s

make64(a)
print ""
start = time.time()
trav(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to travers list is " + timeTaken + " milliseconds"
print s

print "end of pointer List"
