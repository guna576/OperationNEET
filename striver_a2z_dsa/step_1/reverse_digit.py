def fun(n):
    ans = dict()
    ans["String"] = int(str(n)[::-1])
    
    m = n 
    sol = 0
    while m:
        sol = sol*10 + m%10
        m //= 10
    ans["iter"] = sol 
    return ans

n = 1234560
print(f"The Differnt ways of reversing a digit is : {fun(n)}")