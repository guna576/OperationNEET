from functools import reduce
l = [1,2,3,2,1,3,5,6,6,8,8]
print(f"The one missing number appeared only once is {reduce(lambda x,y:x^y,l)}")

# TC : O(N)


