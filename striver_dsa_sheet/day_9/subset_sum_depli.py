class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        st = set()
        def fun(nums, i, n, ans):
            nonlocal st
            if i == n:
                st.add(tuple(ans))
                return 
            fun(nums,i+1,n,ans+[nums[i]])
            fun(nums,i+1,n,ans)
            return 
        nums.sort()
        fun(nums,0,len(nums),[])
        return [list(x) for x in st]

# same as subset sums but it's treated as Brute force
# O(nlogn) + O(2^n)*(O(klogx)) k:avg length and x:size and SC: O(2^n*k) and same for set

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path, res):
            res.append(path)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, path + [nums[i]], res)
        
        nums.sort()
        res = []
        dfs(0, [], res)
        return res
    
# Without using extra set, removing duplicants, just like 3Sum