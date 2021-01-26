'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
#---------------------
# KADANE's ALGORITHM
#----------------------

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        maximum=float('-inf')
        for i in range(len(nums)):
            s+=nums[i]
            maximum=max(maximum,s)
            s=max(s,0)
        return maximum
