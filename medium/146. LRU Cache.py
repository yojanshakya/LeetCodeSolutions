class ListNode:
	def __init__(self, key:int, val: int, next, prev):
		self.val = val
		self.next = next
		self.prev = prev


class LRUCache:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.hashMap = dict()
		self.recentNode = None
		self.nonRecentNode = None

	def get(self, key: int) -> int:
		node = self.hashMap[key]

		if node.prev :
			node.prev.next = node.next
		
		if node.next :
			node.next.prev = node.prev

		node.prev = self.recentNode
		node.next = None

		self.recentNode.next = node
		self.recentNode = node

		return node.val

	def put(self, key: int, value: int) -> None:
		node = ListNode(key, value, None, None)

		if(len(self.hashMap) == self.capacity):
			# remove non recent node
			nodeToBeRemoved = self.nonRecentNode
			self.nonRecentNode = nodeToBeRemoved.next
			self.nonRecentNode.prev = None
			del self.hashMap[nodeToBeRemoved[key]]

		if(len(self.hashMap)> 0):
			node.prev = self.recentNode
			self.recentNode.next = node
		else:
			self.nonRecentNode = node


		self.recentNode = node
		self.hashMap[key] = node


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2) 
lRUCache.get(1)  
lRUCache.put(3, 3) 
lRUCache.get(2)  
lRUCache.put(4, 4) 
lRUCache.get(1)  
lRUCache.get(3)    
lRUCache.get(4)   