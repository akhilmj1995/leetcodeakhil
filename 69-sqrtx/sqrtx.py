class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x
        if x==1:
            return 1
        while(l<r):
          mid=int((l+r)/2)
          temp=int(x/mid)
          if temp==mid:
              return mid
          elif temp<mid :
              r=mid
          else:
              l=mid+1
        return l-1

        

        
          