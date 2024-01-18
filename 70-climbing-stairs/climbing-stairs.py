class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=0,1
        if n==0:
            return n
        for i in range(n):
            a,b=b,a+b
        return b
        
               