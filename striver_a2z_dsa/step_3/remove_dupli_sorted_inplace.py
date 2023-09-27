

def fun(l,n):
    if n < 2: return n, l
    i,j = 0,1 
    while i < n and j < n:
        if l[i] != l[j]:
            # This is the logic man 
            # for [1,2,3] case we replace 2 with 2 and 3 with 3 
            l[i+1], l[j] = l[j], l[i+1]  
            i += 1 
        j += 1 
    return i+1, l

l = [1,2,2,2,3,4,5,6,6,7,8,8]
k,ans = fun(l,len(l))
print(f"The no. of unique elements are {k} and sorted inplace array is : {ans}")

#  TC and SC : O(N) and O(1)