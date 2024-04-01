class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a=1
        i=0
        while a<=n:
            if a==n:
                return True
            a=pow(4,i)
            i+=1
        return False
        