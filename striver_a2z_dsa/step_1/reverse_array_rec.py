

def rev(l, i, j):
    if i >= j: return l 
    l[i],l[j] = l[j],l[i]
    return rev(l,i+1,j-1)

l = [2,1,0]
print(f"The reverse of the {l} is {rev(l, 0, len(l)-1)}")