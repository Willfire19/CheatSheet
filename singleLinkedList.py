# Single Linked List
class Node:
	next = None
	prev = None
	value = None

	def __init__(self, value):
		self.value = value

class SingleLinkedList:
	root = None

	def __init__(self, value):
		self.root = Node(value)

	def __str__(self):
		currentNode = self.root
		result = "[" + str(currentNode.value)
		while currentNode.next != None:
			currentNode = currentNode.next
			result += ", " + str(currentNode.value)
		result += "]"
		return result

	def appendToTail(self, value):
		newNode = Node(value)
		currentNode = self.root
		while currentNode.next != None:
			currentNode = currentNode.next
		currentNode.next = newNode

class DoubleLinkedList:
	root = None

	def __init__(self, value):
		self.root = Node(value)

	def __str__(self):
		currentNode = self.root
		result = "[" + str(currentNode.value)
		while currentNode.next != None:
			currentNode = currentNode.next
			result += ", " + str(currentNode.value)
		result += "]"
		return result

	def appendToTail(self, value):
		newNode = Node(value)
		currentNode = self.root
		while currentNode.next != None:
			currentNode = currentNode.next
		currentNode.next = newNode
		newNode.prev = currentNode

def main():
	linkedList = SingleLinkedList(1)
	linkedList.appendToTail(2)
	linkedList.appendToTail(3)
	linkedList.appendToTail(4)
	linkedList.appendToTail(5)

	doubleList = DoubleLinkedList(5)
	doubleList.appendToTail(4)
	doubleList.appendToTail(3)
	doubleList.appendToTail(2)
	doubleList.appendToTail(1)

	print linkedList
	print doubleList

if __name__ == "__main__":
	main()