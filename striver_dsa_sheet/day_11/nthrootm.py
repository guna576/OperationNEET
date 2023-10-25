def findpow(n,x):
  ans = 1 
  while n:
    if n&1:
      ans *= x
      n -= 1 
    else:
      x *= x 
      n //= 2 
  return ans

def nthrootofm(n,m):
  i = 1
  j = m
  
  while i <= j:
    md = (i+j)//2
    num = findpow(n,md)
    
    if num == m: return md 
    elif num < m: i = md + 1 
    else: j = md - 1 
    
  return -1
  

n,m = 3,27
print(f"The {n}th root of {m} is {nthrootofm(n,m)}")

## TC; O(log2m)*O(log2n) for binary Search and finding power
## SC: O(1)


## The idea is to do BS from 0 to m