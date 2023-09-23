


def fun(a,b):
    if b == 0: return a

    return fun(b,a&b)

a,b = 16, 32
print(f"The GCD/HCF for {a} and {b} is {fun(max(a,b), min(a,b))}")
# TC and SC : O(logɸmin(a,b)), where ɸ is 1.61, O(1)

import math 
print(f"Another way of doing this using math : {math.gcd(b,a)}")