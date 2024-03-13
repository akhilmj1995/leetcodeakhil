class Solution:
    def pivotInteger(self, n: int) -> int:    
        if n==1:
            return 1
        for i in range(2,n):
            m=i*(i+1)//2
            if m==(n*(n+1)//2-m+i):
                return i
        return -1