# we can do this using formula and I'm not interested
class Solution:
    def generate(n):
        l = [[1]*x for x in range(1,n+1)]
        for x in range(2,n):
            for i in range(x-1,0,-1):
                l[x][i] = l[x-1][i] + l[x-1][i-1]
        return l
    
print(f"The pascals triangle is of size {5} is {Solution.generate(5)}")