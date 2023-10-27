
def heapify(l,n,i):
    large = i
    left = 2*i + 1 
    right = 2*i + 2 

    if left < n and l[large] < l[left]:
        large = left 
    if right < n and l[large] < l[right]:
        large = right 
    
    if large != i:
        l[large], l[i] = l[i], l[large]
        heapify(l,n,large)


def heapsort(l,n):
    # first build the max heap
    for i in range((n//2)-1,-1,-1):
        heapify(l,n,i)

    # Now extract one by one by pushing it to end and giving function last - 1 everytime 
    for i in range(n-1,0,-1):
        l[i],l[0] = l[0], l[i]
        heapify(l,i,0)

l = [12, 11, 13, 5, 6, 7]
n = len(l)
heapsort(l,n)
print(f"The sorted list in inc order is {l}")