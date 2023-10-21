class Solution:
    def combinationSum2(self, cans: List[int], x: int) -> List[List[int]]:
        cans.sort()
        res = []
        def backtrack(idx, path):
            if sum(path)==x:
                res.append(path)
                return
            elif sum(path)>x:
                return
            for i in range(idx, len(cans)):
                if i!=idx and cans[i]==cans[i-1]:
                    continue
                backtrack(i+1, path+[cans[i]])
                # Repeated elements are NOT allowed, so idx = i+1 here
        backtrack(0, [])
        return res
        