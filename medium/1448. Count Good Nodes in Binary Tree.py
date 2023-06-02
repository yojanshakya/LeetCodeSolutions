class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

"""
	Time complexity : O(n) where n is total number of nodes
	Space complexity: O(n) because for a binary tree that goes only one side height = n 
"""
class Solution:
	def goodNodes(self, root: TreeNode) -> int:
		
		res = 0

		def backtrack(node, maxTillNow):
			if not node:
				return
			
			if node.val >= maxTillNow:
				res += 1
			
			backtrack(node.left, max(maxTillNow, node.val))
			backtrack(node.right, max(maxTillNow, node.val))

		backtrack(root, 0)

		return res