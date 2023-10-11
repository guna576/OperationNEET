
def merge(l,low,mid,high):
  left = low 
  right = mid+1 
  ans = []
  count = 0
  
  while left <= mid and right <= high:
    if l[left] <= l[right]:
      ans += [l[left]]
      left += 1 
    else:
      ans += [l[right]]
      right += 1 
      count += mid-left+1
    
  while left <= mid:
    ans += [l[left]]
    left += 1 
    
  while right <= high:
    ans += [l[right]]
    right += 1 
  
  for x in range(len(ans)):
    l[low + x] = ans[x]
    
  return count

def ms(l,i,j):
  count = 0
  if i < j:
    m = (i+j)//2
    
    count += ms(l,i,m)
    count += ms(l,m+1,j)
    count += merge(l,i,m,j)
  #   count += 
  return count


l = [5, 4, 3, 2, 1]

print(f"The number of inversions of elements to get a sorted aray is : {ms(l,0,len(l)-1),l}")
# https://leetcode.com/problems/reverse-pairs/description/
# you are finding pairs where i < j and a[i] > a[j] (a[i],a[j]) using merge sort.   