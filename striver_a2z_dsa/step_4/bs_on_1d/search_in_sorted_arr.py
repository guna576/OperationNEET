def fun_rec(l,k,i,j):
    if i > j: return -1 
    m = (i+j)//2
    if l[m] == k: return m 
    elif l[m] < k: return fun_rec(l,k,m+1,j)
    else: return fun_rec(l,k,i,m-1)


def fun_loop(l,k):
    i = 0
    j = len(l)-1

    while i <= j:
        m = (i+j)//2
        if l[m] == k: return m
        elif l[m] < k: i = m+1
        else: j = m-1
    return -1


k,l = 9,[-1,0,3,5,9,12]
print(f"Search for a {k} in sorted {l} is at {fun_loop(l,k)} index")
print(f"Search for a {k} in sorted {l} is at {fun_rec(l,k, 0, len(l)-1)} index")

# O(logN) <-- TC
