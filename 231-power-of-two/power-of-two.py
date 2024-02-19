class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n%2!=0 and n!=1:
            return False
        if n%3==0 or n%5==0:
            return False
        if n%7==0 or n%11==0:
            return False
        for i in range(0,n//2+1):
            if pow(2,i)==n:
                return True
        return False

        