class Solution:
    def majorityElement(nums):
        
        c1,c2 = 0,0
        el2 = float('-inf')
        el1 = el2

        for x in nums:
            if c1 == 0 and x != el2:
                c1 += 1
                el1 = x
            elif c2 == 0 and x != el1:
                c2 += 1
                el2 = x 
            elif x == el1:
                c1 += 1
            elif x == el2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1 
        n = len(nums)
        ans = []
        if nums.count(el1) > n//3:
            ans += [el1]
        if nums.count(el2) > n//3:
            ans += [el2]
        return ans
        
        
print(f"The elements whose count is >(n/3) are {Solution.majorityElement([3,2,3])}")