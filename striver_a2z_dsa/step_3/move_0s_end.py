class Solution:
    def moveZeroes(self, l):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(l)
        if n < 2: return l 

        i = 0
        j = 0

        while i < n and j < n:
            while l[i] == 0 and j < n and l[j] == 0:
                j += 1
            if j < n: 
                l[i],l[j] = l[j],l[i]
            i += 1 
            j += 1 

        return l
    
sol = Solution()
l = [0,1,2,0,3,4,0,4,5,6]
print(f"The array after moiving zeros to end is : {sol.moveZeroes(l)}")

# O(N) and O(1)