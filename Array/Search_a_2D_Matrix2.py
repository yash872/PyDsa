'''
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. The task is to find whether element X is present in the matrix or not.
Example 1:
Input:
N = 3, M = 3
mat[][] = 3 30 38 
         44 52 54 
         57 60 69
X = 62
Output: 0
Explanation: 62 is not present in the matrix, so output is 0
'''
#------------------------------
# Time-> O(M+N) | Sapce-> O(1)
#------------------------------
class Solution:
	def matSearch(self,mat, N, M, X):
    	i = 0 
    	j = M - 1
    	while ( i < N and j >= 0 ): 
    	
    		if (mat[i][j] == X ): 
    	
    			#print("n Found at ", i, ", ", j) 
    			return 1
    	
    		if (mat[i][j] > X ): 
    			j -= 1
    			
    		# if mat[i][j] < x 
    		else: 
    			i += 1
    	
    	#print("Element not found") 
    	# if (i == n || j == -1 )
      return 0 
