class Solution:
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        st = [x for x in range(n)]
        while len(st) > 1:
            i,j = st.pop(),st.pop()
            if M[i][j] == 1:
                st += [j]
                
            elif M[j][i] == 1:
                st += [i]
        if st:
            c = 0
            for i in range(n):
                if M[st[-1]][i] == 1: return -1
                if M[i][st[-1]] == 1: c += 1
            if c == n-1: return st[-1]
            
        return -1

# This is the stack implementation which uses O(N) and O(N)

# we can use the 2 pointer to solve this optimally in O(N) and O(1) but can't make sense

# another approach
#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        c = 0
        for i in range(1,n):
            if M[c][i] == 1: c = i
        
        for i in range(n):
            if i != c and M[c][i] == 1 or M[i][c] == 0: return -1 
        return c


# Most controversal ever