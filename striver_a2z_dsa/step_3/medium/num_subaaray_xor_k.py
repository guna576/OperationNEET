from collections import defaultdict
def fun(l,k):
  d = defaultdict(int)
  d[0] = 1 
  ans = 0
  count = 0
  for x in l:
    ans ^= x 
    count += d[k^ans]
    d[ans] += 1
  return count
print(f"The no of subaaray with xor {6} is {fun([4, 2, 2, 6, 4],6)}")

# TC: O(N) and SC: O(N)