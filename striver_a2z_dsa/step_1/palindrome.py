
def fun(l):
    ans = dict()
    for x in l:
        y = x
        z = 0 
        while x:
            z *= 10 
            z += x%10 
            x //= 10 
        ans[y] = True if y == z else False 
    return ans

n = [123, 121, 1230, 1210, 0000]
print(f"palindrome list : {fun(n)}")