# Stacks and Queues

class Node:
	next = None
	value = None

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class Stack:
	top = None

	def pop(self):
		if self.top != None:
			newTop = self.top.next
			popTop = self.top
			self.top = newTop
			return popTop

	def push(self, value):
		newTop = Node(value)
		newTop.next = self.top
		self.top = newTop

	def peek(self):
		if self.top != None: return self.top.value

class Queue:
	first = None
	last = None

	def enqueue(self, value):
		if self.first == None:
			self.last = Node(value)
			self.first = self.last
		else:
			newNode = Node(value)
			self.last.next = newNode
			self.last = newNode

	def dequeue(self):
		if self.first != None:
			returnNode = self.first
			self.first = self.first.next
			if self.first == None: self.last = None			
			return returnNode

	# enqueue
	# dequeue

def main():
	print "Stacks"
	stack = Stack()
	stack.pop()
	# stack.push(1)
	# stack.push(2)
	# print stack.peek()
	# stack.pop()
	print stack.peek()

	print "Queues"
	queue = Queue()
	queue.enqueue(5)
	queue.enqueue(10)
	print queue.dequeue()

if __name__ == "__main__":
	main()