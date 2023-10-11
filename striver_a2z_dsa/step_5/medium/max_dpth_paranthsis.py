class Solution:
    # Without Stack
    def maxDepth(s):
        count = 0

        ans = 0
        for x in s:
            if x == "(":
                count += 1 
                ans = max(ans,count)
            elif x == ")":
                count -= 1
        return max(count,ans)
    
    # with stack is nothing but puuting "(" and calculating it's length for answer

print(f"The maximum depth of paranthesis that consists of number is {Solution.maxDepth('(1+(2*3)+((8)/4))+1')}")