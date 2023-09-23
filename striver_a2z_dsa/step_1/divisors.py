
def fun(z):
    l = []

    for x in range(1, int(z**0.5) + 1):
        if z%x == 0: l += [x]
        if x*x != z: l += [z//x]
    return l


z = 36
print(f"All the diviors are here : {fun(z)}")

# TC and SC : O(sqrt(z)), O(1)