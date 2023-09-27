# only hashing works for this with positive and negative values 

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



n,l,k = 3,[2,3,5],5

print(f"The longest subarray length using map = {k} is {fun_better(l,k,n)}")
# O(N) and O(N) map