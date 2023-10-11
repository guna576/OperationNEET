
# O((n1+n2 log(n1+n2))) and inserting anything to dict takes O(log(n1+n2)))
def fun_map(l,m):
    d = dict()
    for x in l: d[x] = d.get(x,0) + 1 
    for y in m: d[y] = d.get(y,0) + 1
    ans = []

    for i,j in d.items():
        ans += [i]
    return ans

# O((n1+n2 log(n1+n2))) and inserting anything to set takes O(log(n1+n2)))
def fun_set(l,m):
    return sorted(list(set(l+m)))

# TC : O(n1+n2) and space is no extra 
def fun_p(l,m):
    n1,n2 = len(l), len(m)
    ans = []
    i,j = 0,0
    k = 0
    while i < n1 and j < n2:
        z = 0
        if l[i] < m[j]:
            z = l[i]
            i += 1
        elif l[i] > m[j]:
            z = m[j]
            j += 1 
        else:
            z = l[i]
            i += 1 
            j += 1 
        if k and ans[-1] != z or not k: ans += [z] 
    while i < n1:
        if k and ans[-1] != l[i] or not k:
            ans += [l[i]]
            i+= 1
    while j < n2:
        if k and ans[-1] != m[j] or not k:
            ans += [m[j]]
            j += 1 
    return ans


l = [2,3,4,4,5,11,12]
m = [1,2,3,4,5,6,7,8,9,10]

print(f"Using map : {fun_map(l,m)}")
print(f"Using set : {fun_set(l,m)}")
print(f"using pointers : {fun_p(l,m)}")