# i < j and a[i] > 2*a[j] and ans = (a[i],a[j])
def countInv(l,low,mid,high):
  count = 0
  le = low
  ri = mid + 1 
  
  while le <= mid and ri <= high:
    if l[le] > 2*l[ri]:
      ri += 1 
      count += mid-le+1
    else:
      le += 1
  return count 
        

def merge(l,low,mid,high):
  left = low 
  right = mid+1 
  ans = []
  
  while left <= mid and right <= high:
    if l[left] <= l[right]:
      ans += [l[left]]
      left += 1 
    else:
      ans += [l[right]]
      right += 1 
    
  while left <= mid:
    ans += [l[left]]
    left += 1 
    
  while right <= high:
    ans += [l[right]]
    right += 1 
  
  for x in range(len(ans)):
    l[low + x] = ans[x]
    


def ms(l,i,j):
  count = 0
  if i < j:
    m = (i+j)//2
    
    count += ms(l,i,m)
    count += ms(l,m+1,j)
    count += countInv(l,i,m,j)
    merge(l,i,m,j)
  #   count += 
  return count


l = [4, 1, 2, 3, 1]

print(f"The number of inversions of elements in two times to get a sorted aray is : {ms(l,0,len(l)-1),l}")