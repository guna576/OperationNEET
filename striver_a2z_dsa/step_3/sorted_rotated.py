
def fun(l):
    f = 0 
    for i in range(len(l)-1):
        if l[i] > l[i+1]: f += 1 
    return True if f < 2 else False 


l = [5,6,7,1,2,8,4]

print(f"Is it sorted ? {l} : {fun(l)}")