class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        ans = [-1] * (len(A))
        st = [A[0]]
        for x in range(1,len(A)):
            while st and st[-1] >= A[x]:
                st.pop()
            if st:
                ans[x] = st[-1]
            st += [A[x]]
        return ans
            