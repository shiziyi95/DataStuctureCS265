from node import Node

class Queue:
	def __init__(self):
		self.front = None

	def FRONT(self):
		return self.front

	def ENQUEUE(self,n):
		if self.front == None:
			self.front = n
		else:
			tmp = self.front
			while tmp.next != None:
				tmp = tmp.next
			tmp.next = n
			return
			#tmp = tmp.next
		
	def DEQUEUE(self):
		n = self.front
		n = n.next
		self.front = n
		'''
		while n.next.next != None:
			n = n.next
		n.next = None
		'''
		return

	def EMPTY(self):
		self.front = None
		return 

	def PrintQueue(self):
		print self.front.val
		tmp = self.front
		while tmp.next != None:
			tmp = tmp.next
			print tmp.val
		return

###########
'''
l = Queue()
n = Node(1)
l.ENQUEUE(n)

n.right = Node(2)
n.left = Node(3)
l.ENQUEUE(n.right)
l.ENQUEUE(n.left)
#print l.front.right.val
l.DEQUEUE()
l.PrintQueue()


'''

