from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

"""
	Optimal Solution

	time complexity: O(n)
	space complexity: O(1)

	Algorithm (Try to visualize this):
	1) Select the first Node as p1
	2) Remove p1's next node and make it head (make valid pointers)
	3) Continue until p1 has no next	  

	Note:- Another solution is by using stack which is much easier,
	but has space complexity of O(n)
"""
class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		
		if(not head or not head.next):
			return p1

		p1 = head

		while(p1 and p1.next):
			newHead = p1.next
			p1.next = newHead.next
			
			newHead.next = head
			head = newHead

			pass

		return head
	
solution = Solution()

def printList(node: ListNode):
	while(node):
		print(node.val)
		node = node.next

printList(solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))))
	

