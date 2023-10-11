class Solution:
    def largestOddNumber(num):
        a,b = float('-inf'),-1

        for x in range(len(num)-1,-1,-1):
            val = ord(num[x])
            if val&1:

                return num[:x+1]
        return ""
print(f"The largest odd string is {Solution.largestOddNumber('5433321')}")