# https://www.codingninjas.com/studio/problems/count-with-k-different-characters_1214627?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0

from typing import *
from collections import defaultdict
def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    ans = 0
    i = 0
    j = 0
    d = dict()
    for x in range(len(s)):
        if s[x] not in d:
            i += 1 
            d[s[x]] = 1 
        elif d[s[x]] > 0:
            d[s[x]] += 1
        else:
            d[s[x]] += 1 
            i += 1
        while i > k and j <= x:
            d[s[j]] -= 1
            i -= 1
            if d[s[j]] == 0:
                j += 1 
                break  
            i += 1
            j += 1
        if i == k:
            print(s[j:x+1])
            ans += x-j + 2 - k
    return ans
         
            
# tried hard but not working       

    