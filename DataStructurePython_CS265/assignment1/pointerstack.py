import time
class Node:
	def __init__( self ):
 		self.val = None
		self.next = None

class LinkedStack:
	def __init__( self ):
		self.head = None
		self.tail = None
		
	def PUSH(self,x):
		n = Node()
		n.val = x #creat node with val x
		n.next = self.head
		self.head = n
		return
	def POP(self):
		self.head = self.head.next
		return 

	def printStack(self):
		n = self.head
		i = 0
		while n :
			i += 1
			print str(i) + "th: " + str(n.val)
			n = n.next

	def EMPTY(self):
		while self.head != None:
			self.POP()
		return 
	def MAKENULL(self):
		return LinkedStack()

###############
def iteratedPush(L):
	L.MAKENULL()
	for i in range(64):
		L.PUSH(3)

def iteratedPop(L):
	L.MAKENULL
	while L.head != None:
		L.POP()
	return 
##############
a = LinkedStack()
print "welcome to counting pointerStack: size 64\n"
start = time.time()
iteratedPush(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to iteratedPush(a) list is " + timeTaken + " milliseconds"
print s


print ""
start = time.time()
iteratedPop(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to iteratedPop(a) list is " + timeTaken + " milliseconds"
print s
print "------------------------End of pointerStacks \n"


a.printStack()