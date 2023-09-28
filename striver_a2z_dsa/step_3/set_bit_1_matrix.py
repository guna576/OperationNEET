
# we ahve to set entire row and column to 0 if any element in them is 0
# we are flagging the first element in row and column to 0 on finding 0 anywhere in that.
# then iterating from botto right to start exclusing first col because of overhead
# using col variable to further handle first col zeros 

m=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

r,c = len(m), len(m[0])
col = 0
for i in range(r):
  for j in range(c):
    if m[i][0] == 0: col = 1
    
    if m[i][j] == 0:
      m[i][0] = 0
      m[0][j] = 0 
      
for i in range(r-1,-1,-1):
  for j in range(c-1,0,-1):
    if m[i][0] == 0 or m[0][j] == 0: m[i][j] = 0
  if col: m[i][0] = 0

print(m)

# TC and Sc: O(2*(r+c)) and O(1)