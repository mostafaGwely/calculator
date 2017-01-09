class Queue():
	def __init__(self):
		self.item = [] 
	def enqueue(self,value):
		self.item.insert(0,value)
	def dequeue(self):
		return self.item.pop()
	def is_empty(self):
		return self.item == []