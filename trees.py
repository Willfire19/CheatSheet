# Trees and Graphs

class Node:
	left = None
	right = None
	value = None

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

class BinarySearchTree:
	root = None

	def add(self, value):
		if self.root is None:
			self.root = Node(value)
			return
		else:
			self._add(self.root, value)

	def _add(self, node, value):
		if value < node.value:
			if node.left != None:
				self._add(node.left, value)
			else:
				node.left = Node(value)
		elif value > node.value:
			if node.right != None:
				self._add(node.right, value)
			else:
				node.right = Node(value)

	def deleteTree(self):
		self.root = None

	def find(self, value):
		print value

	def printTree(self):
		if self.root != None:
			self._printTree(self.root)

	def _printTree(self, node):
		if node != None:
			self._printTree(node.left)
			print str(node.value) + ' ',
			self._printTree(node.right)

def main():
	print "Trees and Graphs"
	bst = BinarySearchTree()
	bst.add(5)
	bst.add(2)
	bst.add(9)
	bst.add(1)
	bst.add(3)
	bst.add(7)
	bst.printTree()

if __name__ == "__main__":
	main()