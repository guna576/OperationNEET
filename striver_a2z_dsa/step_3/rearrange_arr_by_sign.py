# 2 pointer inplace should work but not working font know


def fun(l):
    ans = []
    p,n = 0,0

    i = 0 
    
    while i < len(l):
      if i&1:
        while l[n] > -1: n += 1 
        ans += [l[n]]
        n+= 1 
      else:
        while l[p] < 0: p += 1
        ans += [l[p]]
        p+=1
      i += 1
    return ans

l = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]

print(f"The rearranged array as +,-,+ like that with relative order is {fun(l)}")
# O(N) and O(N)

# Expected : [28,-41,22,-8,46,-37,35,-9,18,-6,19,-26,15,-37,14,-10,31,-9]
# output:[28,-41,22,-8,46,-37,35,-9,18,-6,19,-26,15,-37,14,-10,31,-9]