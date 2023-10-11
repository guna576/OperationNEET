import collections
# It is bruteforce mowa
class Solution:
    def beautySum(s):
        ans = 0
        n = len(s)
        for i in range(n-1):
            d = collections.defaultdict(int)
            d[s[i]] += 1
            for j in range(i+1,n):      
                d[s[j]] += 1
                z = max(d.values()) - min(d.values())
                ans += z if z else 0
        return ans
        
print(f"The sum of the beauty of all the substrings[The max freq - min freq atleast 1] is {Solution.beautySum('aabcbaa')}")
# TC: O(N*N*26) and SC: O(26)