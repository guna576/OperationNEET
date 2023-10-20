#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,l,n):
        
        # code here
        cnt = 0
        pro = 0
        l.sort(reverse = True, key = lambda x:(x[2],x[1]))
        mxS = max(x[1] for x in l)
        ans = [-1]*(mxS+1)
        
        for _,d,p in l:
            i = d
            while i > 0 and ans[i] != -1:
                i -= 1
            if i > 0:
                ans[i] = p
        return sum(x for x in ans if x!=-1)

# This is not the final code as it was not submitted becoz of stupidity of GFG
# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#