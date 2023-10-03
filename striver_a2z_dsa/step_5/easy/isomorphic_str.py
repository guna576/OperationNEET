class Solution:
    def isIsomorphic(s,t):
        if len(s) != len(t): return False
        d1 = dict()
        d2 = dict()
        for i in range(len(s)):
            if s[i] in d1:
                if d1[s[i]] != t[i]: return False
            else:
                if t[i] in d2: return False
                d1[s[i]] = t[i]
                d2[t[i]] = s[i]
        return True

print(f"Do both strings are isomorphic: each charater maps in a sequence : {Solution.isIsomorphic('egg','add')}")