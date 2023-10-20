from os import *
from sys import *
from collections import *
from math import *

def fun(l,k):
    n = len(l)
    if k == 1: return max(l)
    if k == n: return min(l)

    st = []
    ans = []
    for i in range(n):
        if st and i - st[0] >= k: st.pop(0)
        while st and l[st[0]] >= l[i]:
            st.pop()
        
        st += [i]
        if i+1 >= k: ans += [l[st[0]]]
    # print(" dfgh ",ans)
    return max(ans)

def maxMinWindow(l,n):
    # Write your code here
    # Return a list of integers
    ans = []
    for i in range(1,n+1):
        ans += [fun(l,i)]
    return ans


# BUg inside the code but the concept is same as maximum sliding window of size k
# https://www.codingninjas.com/studio/problems/max-of-min_982935?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=3
