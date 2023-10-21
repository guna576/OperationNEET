class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        l = [x for x in range(1,n+1)]
        factT = []
        fact = 1
        for i in range(1,n+1):
            fact *= i
            factT += [fact]
        # print(factT)
        k -= 1
        ans= []
        ln = n-2
        while l:
            f = factT[ln]
            q,k = divmod(k,f)
            # print(q,k)
            ans += [l.pop(q)]
            ln -= 1
        # print(ans)
        return "".join([str(x) for x in ans])

# O(n*n) n for traversing l in while and poping is another n
# O(n) + O(n)