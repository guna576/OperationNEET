# https://leetcode.com/problems/roman-to-integer/description/

class Solution:
    def romanToInt(s):
        ans = 0
        d = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        i = 0
        while i < len(s):
            if i==len(s)-1:
                ans += d[s[i]]
           
            elif d[s[i]] < d[s[i+1]]:
                ans += d[s[i+1]] - d[s[i]]
                i += 1
            else:
                ans += d[s[i]]
            i += 1
        return ans

print(f"The numerical vale of roman num is {Solution.romanToInt('MCMXCIV')}")

