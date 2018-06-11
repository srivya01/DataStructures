class Node(object):

	def __init__(self,data):
		self.data = data
		self.height = 0
		self.leftChild = None
		self.rightChild = None

class AVL(object):

	def __init__(self):
		self.root = None


	def insert(self,data):
		self.root = self.insertNode(data,self.root)

	def insertNode(self,data,node):

		if not node:
			return Node(data)

		if data < node.data:
			node.leftChild = self.insertNode(data,node.leftChild)

		else:
			node.rightChild = self.insertNode(data,node.rightChild)

		node.height = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild)) + 1

		return self.settleViolation(data,node)



	def settleViolation(self,data,node):

		balance = self.calculatebalance(node)
		if balance > 1 and data < node.leftChild.data:
			print("left left heavy situation")
			return self.rightRotation(node)

		if balance < -1 and data > node.rightChild.data:
			print(" right right heavy situation")
			return self.leftRotation(node)

		if balance > 1 and data > node.leftChild.data:
			print("left right heavy situation")
			node.leftChild = self.leftRotation(node.leftChild)
			return self.rightRotation(node)

		if balance < -1 and data < node.rightChild.data:
			print("right left heavy situation")
			node.rightChild = self.rightRotation(node.rightChild)
			return self.leftRotation(node)


		return node


	def calculateHeight(self,node):

		if not node:
			return -1

		return node.height;

	#if it returns value > 1 it is left heavy tree and we do a right rotation
	#if it returns value < -1 it is right heavy tree and we do a left rotation 	
	def calculatebalance(self,node):

		if not node:
			return 0

		return self.calculateHeight(node.leftChild) - self.calculateHeight(node.rightChild) 

	def traverseInOrder(self,node):

		if node.leftChild:
			self.traverseInOrder(node.leftChild)
		print("%s" % node.data)

		if node.rightChild:
			self.traverseInOrder(node.rightChild)


	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root)


	def rightRotation(self,node):
		
		print("Rotating to the right on node ", node.data)

		tempLeftChild = node.leftChild
		t = tempLeftChild.rightChild

		tempLeftChild.rightChild = node
		node.leftChild = t

		node.height = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild)) + 1
		tempLeftChild.height = max(self.calculateHeight(tempLeftChild.leftChild),self.calculateHeight(tempLeftChild.rightChild)) + 1

		return tempLeftChild


	def leftRotation(self,node):

		print("Rotating to the left on node ", node.data)

		tempRightChild = node.rightChild
		t = tempRightChild.leftChild

		node.rightChild = t
		tempRightChild.leftChild = node

		node.height = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild)) + 1
		tempRightChild.height = max(self.calculateHeight(tempRightChild.leftChild),self.calculateHeight(tempRightChild.rightChild)) + 1

		return tempRightChild

	def remove(self,data):
		if self.root:
			self.root = self.removeNode(data,self.root)


	def removeNode(self,data,node):
		if not node:
			return node

		if data < node.data:
			node.leftChild = self.removeNode(data,node.leftChild)

		elif data > node.data:
			node.rightChild = self.removeNode(data,node.rightChild)

		else:
			if not node.leftChild and not node.rightChild:
				print("removing a leaf node")
				del node
				return None

			if not node.leftChild:
				print("removing a node with right child")
				tempNode = node.rightChild
				del node 
				return tempNode

			elif not node.rightChild:
				print("removing a node with a left child")
				tempNode = node.leftChild
				del node
				return tempNode

			print("removing a node with 2 children")
			tempNode = self.getPredecessor(node.leftChild)
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data,node.leftChild)

		if not node:
			return node #if the tree had just a single node


		node.height = max(self.calculateHeight(node.rightChild),self.calculateHeight(node.leftChild)) + 1

		balance = self.calculatebalance(node)

		if balance > 1 and self.calculatebalance(node.leftChild) >= 0:
			return self.rightRotation(node)

		if balance > 1 and self.calculatebalance(node.leftChild) < 0:
			node.leftChild = self.leftRotation(node.leftChild)
			return self.rightRotation(node)

		if balance < -1 and self.calculatebalance(node.rightChild) <= 0:
			return self.leftRotation(node)

		if balance < -1 and self.calculatebalance(node.rightChild) > 0:
			node.rightChild = self.rightRotation(node.rightChild)
			return self.leftRotation(node)

		return node

	def getPredecessor(self,node):
		if node.rightChild:
			return self.getPredecessor(node.rightChild)

		return node





avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(5)
avl.insert(6)
avl.insert(15)

avl.traverse()
avl.remove(15)
avl.remove(20)
avl.traverse()