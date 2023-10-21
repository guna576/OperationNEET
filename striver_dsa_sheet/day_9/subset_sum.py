class Solution:
	def subsetSums(self, l, n):
		def sub(l,i,n,ans,sm):
		    if i == n:
		        ans += [sm]
		        return 
		    sub(l,i+1,n,ans,sm+l[i])
		    sub(l,i+1,n,ans,sm)
		      
		    return 
		ans = []
		sub(l,0,n,ans,0)
		return ans
# Just a Simple Pick and Not Pick
# You will get a recusion tree and splitting recursion tree into 2 parts 
# Therefore the TC will be O(2^n) and Space is also O(2^n) 