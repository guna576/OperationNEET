import math
def fun(n):
    ans = dict()
    ans["string"] = len(str(n))
    ans["iter"] = 0
    ans["log"] = math.floor(math.log10(n) + 1)
    m = n 
    while m:
        ans["iter"] += 1 
        m //= 10 

    return ans 

n = 1234567890
print(f"The different ways of counting the digits is : {fun(n)}")
