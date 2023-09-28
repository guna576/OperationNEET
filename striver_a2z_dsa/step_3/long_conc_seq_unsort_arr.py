l = [3, 8, 5, 7, 6]
s = set(l)

ans = float('-inf')
for x in l:
  c = 1
  if x+1 in s and x-1 not in s:
    
    while x + 1 in s:
      c += 1 
      x += 1 
    ans = max(ans, c)
    c = 1 
print(f"The longest number sequence in an unsorted array is {max(c,ans)}")

# TC : O(N) set + O(2N) for worst case in 2 loops 
# Set insertion time O(logN)