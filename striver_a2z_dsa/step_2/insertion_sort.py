def ins_rec_build(l, i, n):
    if i < 1: return l
    if l[i] < l[i-1]:
        l[i], l[i-1] = l[i-1], l[i]
        return ins_rec_build(l, i-1, n)
    else: return l

def ins_rec(l):
    for i in range(1, len(l)):
        l = ins_rec_build(l,i,len((l)))
    return l

def ins(l):
    for i in range(1, len(l)):
        while i > 0 and l[i] < l[i-1]:
            l[i], l[i-1] = l[i-1], l[i]
            i -= 1

    return l

l = [3,4,2,3,6,3,8,5,6,7,0,2]

print(f"The sorted list {sorted(l)} using insertion sort is : {ins(l)}")
# SC and TC: O(1) and O(N**2)

print(f"The sorted list {sorted(l)} using insertion sort using recursion is : {ins_rec(l)}")
# SC and TC: O(N) and O(N**2)