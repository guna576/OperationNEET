class Solution:
    def combinationSum(self, l: List[int], k: int) -> List[List[int]]:
        l.sort()
        ans = set()
        def fun(i,ans,ds,k):
            if i == len(l):
                if k == 0:
                    ans.add(tuple(ds))
                return 
            if l[i] <= k:
                fun(i,ans,ds + [l[i]],k-l[i]) # picking same element untill the left over is greater
            fun(i+1,ans,ds,k)
            

        fun(0,ans,[],k)
        return [list(x) for x in ans]
    
## Our old solution using for 
class Solution:
    def combinationSum(self, l: List[int], k: int) -> List[List[int]]:
        def fun(i,path,ans):
            if sum(path) == k:
                ans += [path]
                return
            if sum(path) > k:
                return 
            for j in range(i,len(l)):
                fun(j,path+[l[j]],ans)
        l.sort()
        ans = []
        fun(0,[],ans)
        return ans
    
# O(2^n*k) and O(2^n*k) where k is average length of arr