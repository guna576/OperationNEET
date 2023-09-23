


def fun(s,i,j):
    if i >= j: return True 
    if s[i] != s[j]: return False 
    return fun(s,i+1,j-1)

s = "abcdcba1"
print(f"{s} Is it pal : {fun(s, 0, len(s)-1)}")
