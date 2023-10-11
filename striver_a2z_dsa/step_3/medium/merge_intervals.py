class Solution:
    
    def merge(m):
        m.sort()
        l = [m[0]]

        for i in range(1,len(m)):
            if m[i][0] > l[-1][-1]: l += [m[i]]
            else: l[-1][-1] = max(l[-1][-1],m[i][-1])
        return l
    
print(f"The merged array is {Solution.merge([[1,3],[2,6],[8,10],[15,18]])}")
# TC and SC: O(NlogN) + O(N) and O(N) auxilluary space