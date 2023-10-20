class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        arr.sort(reverse = True,key=lambda x:x.value/x.weight) # you should know to use value/weight
        ans = 0.0
        we = 0
        for i in range(n):
            if we + arr[i].weight <= W:
                ans += arr[i].value
                we += arr[i].weight
            else:
                ans += (W-we)*(arr[i].value/arr[i].weight)
                break
        return ans

# O(NlogN) and O(N)