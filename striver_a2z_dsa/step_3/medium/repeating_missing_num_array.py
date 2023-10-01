
# We require 2 numbers means need two equations to solve,
# One equation is by sum of numbers and another is by sum of squares

def fun(l,n):
  
  diffSumOfNum = sum(l) - ((n*(n+1))//2) # x-y = diffSumOfNum
  
  # x^2 - y^2 = diffSumOfNumSq
  # (x+y) = diffSumOfNumSq/(x-y) ; where x-y = diffSumOfNum
  diffSumOfNumSq = (sum([x*x for x in l]) - ((n*(n+1)*(2*n+1))//6))//diffSumOfNum  
  
  # (x+y) + (x-y) = diffSumOfNum + diffSumOfNumSq
  # x = sum/2
  repeatingNum = (diffSumOfNum + diffSumOfNumSq)//2
  
  # y = diffSumOfNumSq - x 
  missingNum = diffSumOfNumSq - repeatingNum
  
  return (missingNum, repeatingNum)

l = [3,1,2,5,4,6,7,5]
# 1 2 3 4 5 6 7 8
print(f"The repeating and missing number is {fun(l,len(l))}")