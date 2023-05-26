from typing import List

"""
	Time Complexity : O(n)
	Space Complexity : O(n)
"""
class Solution:
	def maxArea(self, height: List[int]) -> int:
		l,r = 0, len(height) -1 

		solution = 0
		while(l < r):
			h = min(height[l], height[r])
			w = r-l
			solution = max(solution, h*w)
			
			if height[l] < height[r]:
				l += 1
			else: 
				r-=1

		return solution