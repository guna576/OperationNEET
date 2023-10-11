import collections
class Solution:
    def isAnagram(s,t):
        d1,d2 = collections.Counter(s), collections.Counter(t)
        for i,j in d1.items():
            if i not in d2 or j != d2[i]: return False
        for i,j in d2.items():
            if i not in d1 or j != d1[i]: return False 
        return True

        # return sorted([x for x in s]) == sorted([x for x in t])

print(f"Do the two stings can form same thing??? {Solution.isAnagram('anagram','nagaram')}")
