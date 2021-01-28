'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
'''
#-------------------------------
# Time-> O(N) | Space-> O(1)
#-------------------------------

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=j=k=len(nums)-1
        while(i>0 and nums[i-1]>=nums[i]):
            i-=1
        if(i==0):
            nums.reverse()
            return
        i-=1
        while(nums[j]<=nums[i]):
            j-=1
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i+1:])
