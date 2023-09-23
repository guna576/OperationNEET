
def fun(l):
    ans = dict()
    for x in l:
        y = x 
        z = 0
        while y:
            z += (y%10)**3 
            y //= 10 
        ans[x] = True if z == x else False 
    return ans

l = [153,0,170]

print(f"The armstring numbers : {fun(l)}")