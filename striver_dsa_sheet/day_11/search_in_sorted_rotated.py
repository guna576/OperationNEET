class Solution:
    def search(self, l: List[int], t: int) -> int:
        i = 0
        j = len(l)-1

        while i <= j:
            m = (i+j) >> 1 
            # print(i,j)
            if l[m] == t: return m
            if l[i] <= l[m]:# check left side sorted 
                if l[i] <= t and t < l[m]: # check ele found in btw i and m
                    j = m -1
                else:
                    i = m +1 
            else:
                if l[m] < t and t <= l[j]: # check ele found in btw m and j
                    i = m + 1
                else:
                    j = m - 1

        return -1
# '=' plays a role when dealing with single elements
    