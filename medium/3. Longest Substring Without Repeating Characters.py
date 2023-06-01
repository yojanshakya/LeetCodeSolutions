class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		res = 0	
		l, r = 0, 0
		hashMap = {}

		while(r < len(s)):
			if s[r] in hashMap:
				while(s[l] != s[r]):
					del hashMap[s[l]]
					l += 1
				del hashMap[s[l]]
				l+=1

			hashMap[s[r]] = 1 
			res = max(res, len(hashMap))
			
			r += 1

		return res