l = [10, 22, 12, 3, 0, 6]
ans = [l[-1]]
for i in range(len(l)-2,-1,-1):
  if l[i] > l[i+1]:
    ans += [l[i]]
  else:
    l[i] = l[i+1]
print(f"The leaders of the arrays from right side are : {ans[::-1]}")
# O(N) and O(1)
    