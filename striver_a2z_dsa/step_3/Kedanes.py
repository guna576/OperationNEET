
def fun(l):
    cs = 0
    msf = l[0]
    i,j = 0,0
    a,b = 0,0
    for x in range(len(l)):
        if cs < 0:
            cs,a,b = 0,x,x
        cs += l[x]
        b += 1 
        if cs > msf:
            msf = cs
            i,j = a,b
    
    return msf,l[i:j]

l = [-2,1,-3,4,-1,2,1,-5,4]

# With indices in Code 
print(f"The maximum sum subarray with subarray is : {fun(l)}")
# TC and SC: O(n) and O(1)