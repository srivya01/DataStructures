class Stack(object):

	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return self.stack == []

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		data = self.stack[-1]
		del self.stack[-1]
		return data

	def peek(self):
		data = self.stack[-1]
		return data

	def sizeStack(self):
		return len(self.stack)

stack =Stack()
stack.push(1)
stack.push(3)
stack.push(4)
print(stack.sizeStack())
print("Popped :", stack.pop())
print("Popped :", stack.pop())
print(stack.sizeStack())
print(stack.peek())
print("Popped :", stack.pop())


