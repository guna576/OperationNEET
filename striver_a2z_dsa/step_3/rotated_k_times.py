
def fun_right(l,k,n):
    k %= n 
    l[:] = l[n-k:] + l[:n-k]
    return l

def fun_left(l,k,n):
    k %= n 
    l[:] = l[k:] + l[:k]
    return l 

l = [1,2,3,4,5,7,8,9]
k = 12 
print(f"The rotated list after {k} times right is {fun_right(l,k,len(l))}")
l = [1,2,3,4,5,7,8,9]
print(f"The rotated list after {k} times right is {fun_left(l,k,len(l))}")
# TC and SC : O(N) and O(1)