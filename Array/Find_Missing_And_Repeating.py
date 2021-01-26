'''
Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.
'''

class Solution:
    def findTwoElement( self,arr, n): 
        m=0
        r=0
        xor1=0
        for i in range(n):
            xor1^=arr[i]
        for i in range(1,n+1):
            xor1^=i
        
        set_bit= xor1 & ~(xor1 - 1)
        
        for i in range(n):
            if((arr[i]&set_bit)!=0):
                m^=arr[i]
            else:
                r^=arr[i]
        
        for i in range(1,n+1):
            if((i&set_bit)!=0):
                m^=i
            else:
                r^=i
        if m in arr:
            m,r=r,m
        
        return [r,m]
