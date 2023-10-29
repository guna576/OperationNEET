from collections import defaultdict
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, l, k):
        d = defaultdict(int)
		ans = []
		j = 0
		n = len(l)
		cnt = 0
		for i in range(n):
			
			if i < k and d[l[i]] == 0:
				cnt += 1
			if i >= k:
				if d[l[i-k]] == 1:
					cnt -= 1
				d[l[i-k]] -= 1
				if d[l[i]] == 0:
					cnt += 1
			if i+1 >= k: ans += [cnt] 
			d[l[i]] += 1 
			
		return ans
	
# Basic map implimentation ra erri hook