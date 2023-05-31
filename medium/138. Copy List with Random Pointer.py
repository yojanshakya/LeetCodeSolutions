from typing import Optional

class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random

class Solution:
	def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
		
		hashMap = {}
		hashMap[None] = None

		temp = head
		while(temp):
			hashMap[temp] = Node(temp.val)
			temp = temp.next

		temp = head
		while(temp):
			copy = hashMap[temp]
			copy.next = hashMap[temp.next]
			copy.random = hashMap[temp.random]
			temp = temp.next
			
		
		return hashMap[head]
	

node7 = Node(7)
node13 = Node(13)
node11 = Node(11)
node10 = Node(10)
node1 = Node(1)

node7.next = node13
node7.random = None

node13.next = node11
node13.random = node7

node11.next = node10
node11.random = node1

node10.next = node1
node10.random = node11

solution = Solution()
solution.copyRandomList(node7)
