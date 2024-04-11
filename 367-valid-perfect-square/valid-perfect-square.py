class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=0,num
        while left<=right:
            mid=(left+right)//2
            midv=mid**2
            if midv>num:
                right=mid-1
            elif midv==num:
                return True
            else:
                left=mid+1
        return False
            
            
            


        