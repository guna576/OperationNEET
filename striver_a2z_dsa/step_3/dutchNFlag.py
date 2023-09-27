
def fun(l):
    i,j,k = 0,0,len(l)-1 
    while j <= k:
        if l[j] == 0:
            l[i],l[j] = l[j], l[i]
            i += 1 # you can have j incremented becoz sometime i comes to j in future
        elif l[j] == 2:
            l[j], l[k] = l[k], l[j]
            k -= 1 
            j -= 1 # You dont want to move jth location after swap becoz u dont know what u swapped 
        j += 1 
    return l
    
l = [2,0,2,1,1,0]
print(f"The sorted 0,1,2s are {fun(l)}")