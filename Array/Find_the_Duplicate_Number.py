'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
'''
def findDuplicate(self, nums: List[int]) -> int:
    fast = slow = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break
    slow = nums[0]
    while fast!=slow:
        slow = nums[slow]
        fast = nums[fast]
    return fast
