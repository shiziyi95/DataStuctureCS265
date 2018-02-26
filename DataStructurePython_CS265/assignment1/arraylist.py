import time

size = 16
class arrayList:
	def __init__(self) :
		self.data = [None] * size

	def FIRST(self):
		return self.data[0]
			
	def END(self):
		return self.data[size-1] #it strats with 0

	def RETRIVE(self, p):
		return self.data[p]

	def LOCATE(self, val):
		for i in range(size):
			if self.data[i] == val:
				return i

	def NEXT(self, p):
		return self.data[p+1]

	def PREVIOUS(p, L):
		return self.data[p-1]

	def INSERT(self, val, p):
		if (p == 0) and (self.data[p] == None) :
			self.data[0] = val
		if (self.data[p] == None) and (self.data[p-1] == None):
			return "cant insert here"
		for i in range(size-2, p-1, -1):
			#if i != 0:
			self.data[i+1] = self.data[i] #so move one up
		self.data[p] = val
		return
		
	def DELETE(self, p):
		for i in range(p, size-1):
			self.data[i] = self.data[i+1] #so move one done
		return
		


	def MAKENULL(slef):
		return arrayList()

	def PRINTLIST(self):
		for i in range(0, size):
			if self.data[i] != None:
				print str(i) + "th :" +  str(self.data[i])
		return
################
def insertFront(L):
	L.MAKENULL()
	#for p in range(0,size):
	L.INSERT(7,0)

def insertBack(L):
	L.MAKENULL()
	#for p in range(0, size):
	L.INSERT(8,size-1)

def trav(L):
	L.MAKENULL()
	for p in range(0,size):
		L.INSERT(7,p)
	L.FIRST()
	p = 0
	while p != size-1:
		p += 1
		L.data[p]

def iterateDelete(L):
	L.MAKENULL()
	for p in range(0,size):
		L.INSERT(7,p)
	for p in range(0,size):
		L.DELETE(0)
	for p in range(0,size):
		L.INSERT(7,p)
	for p in range(size-1,-1, -1):
		L.DELETE(size)
################
a = arrayList()
'''
a.INSERT(0,0)
a.INSERT(0,0)
a.INSERT(0,0)
a.INSERT(0,0)

a.INSERT(4, 4)
a.INSERT(5, 5)
#a.INSERT(888, 2)
a.DELETE(0)
'''
iterateDelete(a)



print "welcome to counting arraylist:\n"
start = time.time()
insertFront(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to insertFront list is " + timeTaken + " milliseconds"
print s

start = time.time()
insertBack(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to insertBack list is " + timeTaken + " milliseconds"
print s

start = time.time()
trav(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to traverse list is " + timeTaken + " milliseconds"
print s

start = time.time()
iterateDelete(a)
stop = time.time()
timeTaken=(stop-start)*1000; #time.time() gives time in s, so convert to ms

timeTaken="{:.4f}".format(timeTaken)

s = "Time taken to insertFront list is " + timeTaken + " milliseconds"
print s


#a.PRINTLIST()
