# Brute force : TC : O(n*n) and SC : O(1) (two for loops)

class Solution:
    @staticmethod
    def twoSum(l,k):
        # TC : O(n) SC: O(n)
        d = dict()
        for i in range(len(l)):
            if k-l[i] in d:
                return [d[k-l[i]],i]
            else:
                d[l[i]] = i 
print(f"the two sum answer indises are {Solution.twoSum([1,2,3,4,5],4)}")