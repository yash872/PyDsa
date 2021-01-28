'''
Given an array of integers. Find the Inversion Count in the array. 
Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Example 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
'''
#---------------------------------
# Time-> O(nLogn) | Space-> O(n)
#---------------------------------
def mergesort(a,temp_a,left,right):
    inv_count=0
    if(left<right):
        mid=(left+right)//2
        inv_count+=mergesort(a,temp_a,left,mid)
        inv_count+=mergesort(a,temp_a,mid+1,right)
        inv_count+=merge(a,temp_a,left,mid,right)
    return inv_count

def merge(a,temp_a,left,mid,right):
    i=k=left
    j=mid+1
    inv_count=0
    while(i<=mid and j<=right):
        if(a[i]<=a[j]):
            temp_a[k]=a[i]
            i+=1
            k+=1
        else:
            temp_a[k]=a[j]
            inv_count+=(mid-i+1)
            j+=1
            k+=1
    while(i<=mid):
        temp_a[k]=a[i]
        i+=1
        k+=1
    while(j<=right):
        temp_a[k]=a[j]
        j+=1
        k+=1
    for loop_var in range(left,right+1):
        a[loop_var]=temp_a[loop_var]
