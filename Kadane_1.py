class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        mini = float('-inf') 
        ##Your code here
        su = 0
        maximum = arr[0]
        for i in range(0,len(arr)):
            su += arr[i]
            maximum = max(su,maximum)
            if(su < 0):
                su = 0
        return maximum