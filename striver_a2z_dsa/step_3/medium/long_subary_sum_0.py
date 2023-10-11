
def fun(l,n):
    d = dict()
    ans = float('-inf')
    currSum = 0
    for i in range(n):
        currSum += l[i]
        if currSum == 0: ans = max(ans, i+1)
        elif currSum in d: ans = max(ans, i-d[currSum])
        else: d[currSum] = i 
    return ans


l = [6, -2, 2, -8, 1, 7, 4, -10]
print(f"The longst subarray with sum 0 is {fun(l,len(l))}")

# Tc: O(N) and SC: O(N)