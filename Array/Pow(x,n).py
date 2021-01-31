'''
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
'''
#--------------------------------------------
# Time-> O(Logn) , No of bits in the Power
#--------------------------------------------
# ---------  Modulo Method ------------------
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res,power = 1.0,n
        if(power<0):
            power = -1*power
        while(power>0):
            if(power%2==1):
                res = x*res
                power -=1
            else:
                x = x*x
                power = power/2
        if (n<0):
            res = (1/res)
        return res
        
#------------- Bit Manipulation ---------------
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res,power = 1.0,n
        if(power<0):
            power = -power
            x = (1/x)
            
        while(power):
            if (power & 1):
                res = res*x
            x = x*x
            power = power >> 1
        return res
