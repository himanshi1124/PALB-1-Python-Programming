#Given a number x and an array of integers arr, find the smallest subarray with sum greater than the given value. If such a subarray do not exist return 0 in that case.

class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
       
        curr_sum = 0
        min_len = n + 1
        
       
        left = 0
        
       
        for right in range(n):
            
            curr_sum += arr[right]
            
            
            while curr_sum > x:
                
                min_len = min(min_len, right - left + 1)
                
               
                curr_sum -= arr[left]
                left += 1
                
        # If no such subarray is found, return 0
        return min_len if min_len <= n else 0
