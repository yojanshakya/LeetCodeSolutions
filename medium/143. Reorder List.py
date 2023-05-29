from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseList(self, head: Optional[ListNode]):
		if(not head or not head.next):
			return head
		
		p1 = head

		while(p1.next):
			newHeadNode = p1.next
			p1.next = newHeadNode.next
			
			newHeadNode.next = head
			head = newHeadNode

		return head
	
	def findMidOfLinkedList(self, head: Optional[ListNode]):
		if(not head or not head.next or not head.next.next):
			return head
		
		# turtoise and hare algorithm
		turtoise = head
		hare = head

		while(hare and hare.next):
			turtoise = turtoise.next
			hare = hare.next.next

		return turtoise


	def reorderList(self, head: Optional[ListNode]) -> None:
		if(not head or not head.next or not head.next.next):
			return
		

		mid = self.findMidOfLinkedList(head)
		# separate the main linked list from mid
		nodeBeforeMid = head
		while(nodeBeforeMid.next != mid):
			nodeBeforeMid = nodeBeforeMid.next

		nodeBeforeMid.next = None

		reversedmid = self.reverseList(mid)

		p1 = head
		p2 = reversedmid

		while(p1 and p2):
			tempP1 = p1
			tempP2 = p2

			p1 = p1.next
			p2 = p2.next

			tempP1.next = tempP2
			tempP2.next = p1 if p1 else tempP2.next

			
solution = Solution()

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
solution.reorderList(node)

print(node)