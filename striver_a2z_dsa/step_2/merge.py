

def merge(l,low,mid,high):
    i = low 
    j = mid + 1 
    tmp = []

    while i <= mid and j <= high:
        if l[i] <= l[j]:
            tmp += [l[i]]
            i += 1 
            
        else:
            tmp += [l[j]]
            j += 1 
            

    while i <= mid:
        tmp += [l[i]]
        i += 1 
    while j <= high:
        tmp += [l[j]]
        j += 1 
    
    for x in range(low, high + 1):
        l[x] = tmp[x-low]


def ms(l, i, j):
    if i >= j: return 
    m = (i+j)//2 
    ms(l, i, m)
    ms(l, m + 1, j)
    merge(l,i,m,j)

l = [3,4,2,3,6,3,8,5,6,7,0,2]
ms(l, 0, len(l)-1)
print(f"The sorted list {sorted(l)} using merge sort is : {l}")

# TC and SC : O(NlogN) and O(N) Auxilary space