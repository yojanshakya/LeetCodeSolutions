from typing import List

"""
Time Complexity : O(logn)
Space Complexity : O(1)
"""
class Solution:
	def findMin(self, nums: List[int]) -> int:
		l, r = 0, len(nums)-1
		result = nums[l]

		while(l<=r):
			mid = (l + r) // 2
			result = min(nums[mid], result)

			# left portion is sorted
			if(nums[r] <= nums[mid] ) : 
				l = mid+1
			# right portion is sorted
			else:
				r = mid-1
		
		return result
	
solution = Solution()
solution.findMin([4,5,6,7,0,1,2])