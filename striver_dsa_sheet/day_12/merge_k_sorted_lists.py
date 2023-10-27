from heapq import *
def mergeKSortedArrays(l, k:int):
	# Write your code here.
	# kArrays is a list of 'k' lists.
	# Return a list.
	ans = []
	pq = []

	for x in range(k):
		heappush(pq, (l[x][0],0,x))
	while pq:
		data,i,k = heappop(pq)
		ans += [data]
		if i+1 < len(l[k]):
			heappush(pq,(l[k][i+1],i+1,k))
	return ans

# O(n*m log(m)) and O(n*m)