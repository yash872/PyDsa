'''
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''
#-------------------------------
# Time-> O(MxN) | Space-> O(1)
#-------------------------------

class Solution(object):
    def setZeroes(self, matrix):
        col_flag=0
        R=len(matrix)
        C=len(matrix[0])
        
        for i in range(R):
            if(matrix[i][0]==0):
                col_flag=1
            for j in range(1,C):
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(R-1,-1,-1):
            for j in range(C-1,0,-1):
                if( not matrix[i][0] or not matrix[0][j]):
                    matrix[i][j]=0
            if(col_flag):
                matrix[i][0]=0
        return
