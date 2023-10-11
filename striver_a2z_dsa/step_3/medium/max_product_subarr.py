class Solution:
    def maxProduct(nums):
        suf = 1
        pref = 1 
        ans = float('-inf')

        n = len(nums)

        for i in range(n):
            if suf == 0: suf = 1
            if pref == 0: pref = 1

            suf *= nums[n-i-1]
            pref *= nums[i]

            ans = max(ans, suf, pref)
        return ans
    
print(f"The maximum product subaaray is {Solution.maxProduct([1,2,-3,0,-4,-5])}")

# https://leetcode.com/problems/maximum-product-subarray/description/

# There is a solution using Kedanes algo type but too unrealistic and memorizable