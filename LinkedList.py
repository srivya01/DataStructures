class Node(object):
	
	def __init__(self,data):
		self.data = data
		self.nextNode = None

class Linkedlist(object):

	def __init__(self):
		self.head = None
		self.size = 0
	
	def insertStart(self,data):
		self.size = self.size + 1
		
		newNode = Node(data)
		
		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode


	def size(self):
		return self.size

	def size1(self):
		actualNode = self.head
		size = 0

		while actualNode is not None:
			size+=1
			actualNode = actualNode.nextNode

		return size


	def remove(self,data):
		if self.head is None:
			return
		self.size = self.size -1

		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode
		
		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode
			self.head = previousNode


	def insertEnd(self,data):
		self.size = self.size + 1
		newNode = Node(data)
		actualNode = self.head

		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode

	def traverselist(self):
		actualNode = self.head

		while actualNode is not None:
			print("%d" % actualNode.data)
			actualNode = actualNode.nextNode


linkedlist = Linkedlist()
linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverselist()
linkedlist.remove(3)
linkedlist.traverselist()

print(linkedlist.size1())



