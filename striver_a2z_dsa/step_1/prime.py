
# No need to go till int(n**0.5); If it's perfect int then it divides the number and if not int defini
def fun(n):
    for x in range(2,int(n**0.5)+1):
        if n%x == 0: return False 
    return True

n = 2 
print(f" is this prime : {fun(n)}")