## This is more voting algorithm, have to remember ra Shiv
## WE can do this using hashmaps with TC: O(NlogN)[putting elements in map] + O(N)[traversing over the list]
# and SC: O(N) using map kadha

class Solution:
    def majorityElement(nums):
        cnt = 0
        el = 0

        for x in nums:
            if cnt == 0:
                cnt += 1
                el = x
            elif x == el:
                cnt += 1
            else:
                cnt -= 1 
        return el
    
print(f"The element whose count > (size/2) is {Solution.majorityElement([2,2,1,1,1,2,2])}")
# TC: O(N) and SC: O(1)