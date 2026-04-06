#Given an array arr[] of positive integers, where each value represents the number of
#chocolates in a packet. Each packet can have a variable number of chocolates. There
#are m students, the task is to distribute chocolate packets among m students such that -
#i. Each student gets exactly one packet.
#ii. The difference between maximum number of chocolates given to a student and
#minimum number of chocolates given to a student is minimum and return that minimum possible difference.

class Solution:
    def findMinDiff(self, A, M):
       
        N = len(A)
        
       
        if M == 0 or N == 0:
            return 0
        
       
        A.sort()
        
       
        if N < M:
            return -1
        
       
        min_diff = float('inf')
        
      
        for i in range(N - M + 1):
           
            current_diff = A[i + M - 1] - A[i]
            
           
                
        return min_diff
