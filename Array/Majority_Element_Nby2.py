'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example:
  Input: nums = [2,2,1,1,1,2,2]
  Output: 2
'''
#----------------------------
# Time-> O(N) | Space-> O(1)
#----------------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m_num=0
        m_cnt=0
        for val in nums:
            if(m_num==val):
                m_cnt+=1
                
            elif(m_cnt==0):
                m_num=val
                m_cnt+=1
                
            else:
                m_cnt-=1
               
        return m_num
