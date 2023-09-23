

def fun(n):
    if n <= 1: return n 
    return fun(n-1) + fun(n-2)


n = 10 

print(f"The fibonacci series till the {n}th term is {fun(n)}") 
# we can only print nth fibonacci series with resursion

