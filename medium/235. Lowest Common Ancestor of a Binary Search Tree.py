class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		
		minNode = p if min(p.val, q.val) == p.val else q
		maxNode = p if minNode == q else q

		temp = root
		while(temp):
			if minNode.val <= temp.val and temp.val <= maxNode.val:
				return temp
			elif temp.val < minNode.val:
				temp = temp.right
			else:
				temp = temp.left				
				pass
		
		return None
				  