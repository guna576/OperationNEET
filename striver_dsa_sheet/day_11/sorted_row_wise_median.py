
def findNum(l,r,c,x):
  ans = 0
  for row in range(r):
    i = 0
    j = c-1
    while i <= j:
      m = (i+j)//2
      if l[row][m] <= x:
        i = m + 1 
      else:
        j = m - 1 
    ans += i
  return ans

def findMed(l,r,c):
  i = 0
  j = c*r - 1 
  
  while i <= j:
    md = (i+j)//2
    cnt = findNum(l,r,c,md)
    if cnt <= (r*c//2):
      i = md + 1 
    else:
      j = md - 1 
  return i

r = 3
c = 3
l = [[1, 3, 8],[2, 3, 4],[1, 2, 5]]

print(f"The median of l is {findMed(l,r,c)}")

##  O(row*log col)
## O(1)