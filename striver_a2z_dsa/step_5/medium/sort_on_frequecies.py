import collections
class Solution:
    def frequencySort(s):
        l = list(collections.Counter(s).items())
        l.sort(reverse = True, key = lambda x:x[-1])
        return "".join([x[0]*x[1] for x in l])
    
print(f"The sorted string based on frequencies of letters in desc order {Solution.frequencySort('tree')}")


# TC: O(n) + O(26log26) and SC: O(n)

    