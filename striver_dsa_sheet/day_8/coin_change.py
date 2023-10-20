class Solution:
	def minCoins(self, coins, M, V):
		# code here
		l = [0]*M
		i = 0
        while V and i < M:
            if V >= coins[i]:
                l[i] = V//coins[i]
                V %= coins[i]
            # print(V)
            i += 1
            
        # print(l)
        return sum(l) if not V else -1

# o(V) and O(1) 

## This problme can be solved using Dp as well but the greedy apporach only works if denominations were lke
# {1,2,5,10,20,50,100,500,1000} as two adjacent numbers cannot add to form next number