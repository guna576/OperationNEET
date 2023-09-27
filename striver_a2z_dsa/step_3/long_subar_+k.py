from collections import defaultdict
def fun_better(l,k,n):
    d = dict()
    s = 0
    mc = 0
    for i in range(n):
        s += l[i]
        if s == k:
            mc = max(1+i,mc)
        elif s-k in d:
            mc = max(mc, i-d[s-k]+1)
        d[s] = i 
    return mc

# This is using 2 pointers (optimal)
def fun(l,k,n):
    sm = 0
    ans = 0 
    i,j = 0,0
    while i< n and j < n:
        sm += l[j]
        while sm > k:
            i += 1 
            sm -= l[i]
        if sm == k:
            ans = max(ans, j-i+1)
        j += 1 
    return max(ans,j-i+1)

n,l,k = 3,[2,3,5],5

print(f"The longest subarray length = {k} is {fun(l,k,n)}")
# O(N) and O(1) 2 pointer
print(f"The longest subarray length using map = {k} is {fun_better(l,k,n)}")
# O(N) and O(N) map