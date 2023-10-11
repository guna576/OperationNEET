# Bro, we can do alot of optimizations further depends on situation
class Solution:
    def threeSum(arr):
        # ans = []
        # l.sort()
        # i = 0
        # n = len(l)
        # while i < n-2:
        #     if i > 0 and l[i] == l[i-1]: continue
        #     x = l[i]
        #     left = i+1
        #     right = n-1
        #     while left < right:
        #         y,z = l[left], l[right]
        #         if x + y + z == 0:
        #             ans += [[x,y,z]]
        #             left += 1
        #             while left < right and l[left] == l[left+1]: left += 1
        #         elif x + y + z < 0:
        #             left += 1
        #         else:
        #             right -= 1
        #     i += 1
        # return ans


        ans = []
        arr.sort()
        n = len(arr)
        for i in range(n):
            # remove duplicates:
            if i != 0 and arr[i] == arr[i - 1]:
                continue

        # moving 2 pointers:
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = arr[i] + arr[j] + arr[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [arr[i], arr[j], arr[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    # skip the duplicates:
                    while j < k and arr[j] == arr[j - 1]:
                        j += 1
                    while j < k and arr[k] == arr[k + 1]:
                        k -= 1

        return ans
    
print(f"The sets of x+y+z = 0 in the array is {Solution.threeSum([-1,0,1,2,-1,-4])}")

# TC: O(NlogN) + O(N^2) and SC: O(1) exclusing output array
        