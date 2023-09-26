def quick(l, low, high):
    pivot = l[low]
    i = low 
    j = high 
    while i < j:
        while i <= high-1 and pivot >= l[i]:
            i += 1 

        while j >= low+1 and pivot < l[j]:
            j -= 1 

        if i < j:
            l[i],l[j] = l[j], l[i]
    l[low], l[j] = l[j], l[low]
    return j

def qs(l, i, j):
    if i < j:
        p = quick(l,i,j)
        qs(l,i,p-1)
        qs(l,p+1,j)

l = [3,4,2,3,6,3,8,5,6,7,0,2]
qs(l, 0, len(l)-1)
print(f"The sorted list {sorted(l)} using Quick sort is : {l}")

#TC and SC: O(NlogN) and O(1) + O(N) auxillary space
# Worst TC: O(N**2) if either pivot is smallest or largest or array is in reverse ASC/DESC order


