'''
Given two sorted arrays arr1[] and arr2[] of sizes N and M in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

Example 1:

Input: 
N = 4, arr1[] = [1 3 5 7] 
M = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.
'''
#-------------------------------------------
# Optimize - Caomparison + Insertion  O(mn)
#-------------------------------------------
def merge(arr1,arr2,n,m):
    for i in range(n):
        if(arr1[i]>arr2[0]):
            arr1[i],arr2[0]=arr2[0],arr1[i]
            
            first=arr2[0]
            k=1
            while(k<m and arr2[k]<first):
                arr2[k-1]=arr2[k]
                k+=1
            arr2[k-1]=first


#---------------------------------------------
# Most Optimize - Gap Method  O((m+n)Log(m+n))
#---------------------------------------------
def merge(arr1,arr2,n,m):
    def nextgap(gap):
        if(gap<=1):
            return 0
        else:
            return (gap//2)+(gap%2)
        
    gap=m+n
    gap=nextgap(gap)
    
    while(gap>0):
        i=0
        while(i+gap<n):
            if(arr1[i]>arr1[i+gap]):
                arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
            i+=1
        
        j = gap-n if gap>n else 0
        while(j<m and i<n):
            if(arr1[i]>arr2[j]):
                arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
            j+=1
        
        if(j<m):
            j=0
            while(j+gap<m):
                if(arr2[j]>arr2[j+gap]):
                    arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
                j+=1
        
        gap=nextgap(gap)
