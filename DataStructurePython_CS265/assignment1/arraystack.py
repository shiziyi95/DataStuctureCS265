import time
size = 32
class arrayStack:
	def __init__(self) :
		self.data = [None]* size

	def TOP(self):
		return self.data[0]

	def PUSH(self, x):
		for i in range(size-2,-1, -1):
			self.data[i+1] = self.data[i] #so move one up
		self.data[0] = x

	def POP(self):
		#.data[0] = None
		for i in range(0,size-1):
			self.data[i] = self.data[i+1] #so move one up
		self.data[size-1]  = None
		return
	
	def EMPTY(self):
		while self.top() != None:
			self.pop();
		return 

	def MAkENULL(self):
			return arrayStack()

	def printStack(self):
		for i in range(0,size):
			if self.data[i] == None:
				return
			print str(i) + "th: " + str(self.data[i])

###########

def iteratedPush(S):
	S.MAkENULL()
	for i in range(size):
		S.PUSH(7)

def iteratedPop(S):
	S.MAkENULL()
	for i in range(size):
		S.POP()

#################

a = arrayStack()

print "welcome to counting arrayStack: size 32\n"
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
print "------------------------End of arrayStack"

a.printStack()
