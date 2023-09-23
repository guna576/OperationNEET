

def sm(x):
    if x == 0: return x 
    return x + sm(x-1)

def fact(x):
    if x == 1: return x 
    return x * fact(x-1)

n = 7 

print(f"The sum of {7} nubers is : {sm(n)}")
print(f"The factorial of {n} is : {fact(n)}")