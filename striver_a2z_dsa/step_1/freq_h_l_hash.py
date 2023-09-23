from collections import Counter, defaultdict
def fun(l):
    d = Counter(l)
    mn = 9999999
    mx = -9999999
    mnele = 0
    mxele = 0
    for i,j in d.items():
        if j < mn:
            mn = j 
            mnele = i 
        if j > mx:
            mx = j 
            mxele = i 
    print(f"The minimum element is {mnele} with frequency is {mn}")
    print(f"The maximum element is {mxele} with frequency is {mx}")

l = [1,2,3,2,1,2,3,4,5,6,4,3,2]

fun(l)