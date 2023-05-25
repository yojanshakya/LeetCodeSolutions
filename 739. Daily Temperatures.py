from typing import List

"""
	Optimal Solution
	Spacke Complexity : O(n)
	Time Complexity: O(n) 
"""
class Solution:
	def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
		solution = [ 0 for i in range(len(temperatures))]
		stack = []

		for i, num in enumerate(temperatures):

			while(len(stack) > 0 and stack[-1][0] < num):
				_, indexOfTos = stack.pop()
				solution[indexOfTos] = i - indexOfTos

			stack.append((num, i))

		return solution

			


			

			

