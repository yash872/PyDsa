'''
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.
Example1:
  Input: [1,3,2,3,1]
  Output: 2
'''
#-------------------------------
# Time-> O(nLogn)  Space-> O(n)
#-------------------------------

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def merge(nums,temp,low,mid,high):
            cnt=0
            i,j=low,mid+1
            for i in range(low,mid+1):
                while(j<=high and nums[i] > 2*(nums[j])):
                    j+=1
                cnt += (j - (mid+1))
            
            left,right = low,mid+1
            k=left
            while(left<=mid and right<=high):
                if(nums[left]<=nums[right]):
                    temp[k]=nums[left]
                    left+=1
                    k+=1
                else:
                    temp[k]=nums[right]
                    right+=1
                    k+=1
            while(left<=mid):
                temp[k]=nums[left]
                left+=1
                k+=1
            while(right<=high):
                temp[k]=nums[right]
                right+=1
                k+=1
            
            for i in range(low,high+1):
                nums[i]=temp[i]
            
            return cnt
    
        def mergeSort(nums,temp,low,high):
            cnt=0
            if(low<high):
                mid=(low+high)//2
                cnt += mergeSort(nums,temp,low,mid)
                cnt += mergeSort(nums,temp,mid+1,high)
                cnt += merge(nums,temp,low,mid,high)
            return cnt
        
        n=len(nums)
        temp=[0]*n
        return mergeSort(nums,temp,0,n-1)
