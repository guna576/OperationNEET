def fun(l,n):
    c,nc = 0,0 
    for x in l:
        if x:
            c += 1
            continue  # learn to use continue better 
        nc = max(nc,c)
        c = 0
    return max(nc,c)   # learn to return like this when counting cummulative

l = [1,1,0,1,1,1,0,1,0,1,1,1,1]
print(f"The max consicutive ones we have are {fun(l,len(l))}")