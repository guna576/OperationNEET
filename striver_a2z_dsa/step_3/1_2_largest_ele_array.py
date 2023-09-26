def fun(l):
    a = l[0]
    for x in l: a = max(a,x)
    b = -1 
    for x in l:
        if x != a and x > b: b = x 
    return a,b

l = [3,4,1,2,7,8]

print(f"The 1st and second largest elements in {l} are {fun(l)}")