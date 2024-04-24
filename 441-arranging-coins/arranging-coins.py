class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        if n==1:
            return n
        for i in range(1,n):
            if n<i:
                break
            count+=1
            n-=i
        return count

