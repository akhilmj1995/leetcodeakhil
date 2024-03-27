class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        a=0
        i=0
        while a<n:
            a=pow(3,i)
            if a==n:
                return True
            i+=1
        return False