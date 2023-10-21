class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def fun(id, n, t, ans):
            print(t)
            # if t[:] == t[::-1]:
            #     ans += [t]
            if id == n:
                ans += [t]
                return 
            for i in range(id,n):
                z = s[id:i+1]
                if z == z[::-1]:
                    fun(i+1, n,t + [z], ans)

        fun(0, len(s), [], ans)
        return ans

# O(2^n)*k*n and we can reduce that n on doining 2 pointer check for ispalindrome
# O(2^n)*k space 