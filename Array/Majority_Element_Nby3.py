'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?
Example 1:
  Input: nums = [3,2,3]
  Output: [3]
Example 2:
  Input: nums = [1,2]
  Output: [1,2]
'''
#-----------------------------
# Time->O(N) | Sapce->O(1)
#-----------------------------
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m_num1,m_num2,m_cnt1,m_cnt2= None,None,0,0
        n=len(nums)
        
        for val in nums:
            if(m_num1==val):
                m_cnt1+=1
            elif(m_num2==val):
                m_cnt2+=1
            elif(m_cnt1==0):
                m_num1=val
                m_cnt1+=1
            elif(m_cnt2==0):
                m_num2=val
                m_cnt2+=1
            else:
                m_cnt1-=1
                m_cnt2-=1
        
        return [ele for ele in (m_num1,m_num2) if nums.count(ele) > (n//3)]
