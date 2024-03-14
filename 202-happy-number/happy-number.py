class Solution:
    def isHappy(self, n: int) -> bool:
        a=0
        while a<10:
           k=0
           for i in str(n):
             k+=int(i)**2
             print(k)
           if k==1:
              return True
           n=k
           a+=1  
        return False

