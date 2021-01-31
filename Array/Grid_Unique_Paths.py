'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''
#-------- Recursion ------------------
# Time-> O(2^m+n-2) | Space-> O(1)
#--------------------------------------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        i,j=0,0
        def paths(i,j,m,n,dp):
            #Base Case
            if(i==(m-1) and j==(n-1)):
                return 1
            if(i>=m or j>=n):
                return 0
            else:
                return paths(i+1,j,m,n,dp)+paths(i,j+1,m,n,dp)
                
        return paths(i,j,m,n,dp)
    
#-------- Recursion + DP ------------------
# Time-> O(m x n) | Space-> O(m x n)
#------------------------------------------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)] for j in range(m)]
        i,j=0,0
        def paths(i,j,m,n,dp):
            #Base Case
            if(i==(m-1) and j==(n-1)):
                return 1
            if(i>=m or j>=n):
                return 0
            
            if(dp[i][j]!=-1):
                return dp[i][j]
            else:
                dp[i][j]=paths(i+1,j,m,n,dp)+paths(i,j+1,m,n,dp)
                return dp[i][j]
        return paths(i,j,m,n,dp)
        
#-------- Combinatorics ------------------
# Time-> O(m-1) or O(n-1) | Space-> O(1)
#-----------------------------------------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N = m+n-2
        r = m-1
        res=1
        # --- Calculate NCr ---
        for i in range(1,r+1):
            res = res*(N-r+i)/i
        return int(res)
