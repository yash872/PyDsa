'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

def sortColors(self, nums: List[int]) -> None:
    low=mid=0
    n=len(nums)
    high=n-1
    while(mid<n and mid<=high):
        if(nums[mid]==0):
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif(nums[mid]==1):
            mid+=1
        else:
            nums[high],nums[mid]=nums[mid],nums[high]
            high-=1
