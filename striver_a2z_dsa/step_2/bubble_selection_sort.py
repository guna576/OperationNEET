
def todo_bub(l,)
def bub_rec(l):
    return l


def bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l

def selection(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] > l[j]: l[i], l[j] = l[j], l[i]
    return l

l = [1,2,3,4,5,3,2,1,66,3,9,8]

print(f"The sorted list using bubble sort is : {bubble(l)}")
# TC and SC : O(N**2) and O(1) [Inplace, stable, comparision]

print(f"The sorted list using bubble sort recusion is : {bub_rec(l)}")

print(f"The sorted list using selection sort is : {selection(l)}")
# TC and SC: O(N**2) and O(1) [Same as above]


print(f"The sorted list using selection sort recusion is : {sel_rec(l)}")