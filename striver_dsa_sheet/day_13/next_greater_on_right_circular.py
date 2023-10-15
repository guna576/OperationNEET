
l = [5, 7, 1, 2, 6, 0]
n = len(l)
st = []

ans = [-1] * n

for i in range(2*n-1,-1,-1):
  while st and st[-1] <= l[i%n]:
    st.pop()
  if i < n:
    if st:
      ans[i] = st[-1]
  st += [l[i%n]]
  
print(ans)
    

# O(2N + 2N) and O(N)
# tough to remember but the concept can be useful even for non circluar