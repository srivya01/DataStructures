class Queue(object):

	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self,data):
		self.queue.append(data)

	def dequeue(self):
		data = self.queue[0]
		del self.queue[0]
		return data

	def peek(self):
		data = self.queue[0]
		return data

	def sizequeue(self):
		return len(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(4)
print(queue.sizequeue())
print("Popped :", queue.dequeue())
print("Popped :", queue.dequeue())
print(queue.sizequeue())
print(queue.peek())
print("Popped :", queue.dequeue())


