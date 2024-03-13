class Solution:
    def pivotInteger(self, n: int) -> int:    
        sum=n*(n+1)//2
        k=math.sqrt(sum)
        if k%int(k)==0:
            return int(k)
        return -1