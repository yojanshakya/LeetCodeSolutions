from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

"""
	Space Complexity: O(1)
	Time Complexity: O(n)
"""
class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		if not head.next:
			return None

		tempHead = ListNode(0,head)

		p1 = tempHead
		p2 = head

		while n != 0:
			p2 = p2.next
			n -= 1

		while p2:
			p1 = p1.next
			p2 = p2.next 

		p1.next = p1.next.next
		return tempHead.next
