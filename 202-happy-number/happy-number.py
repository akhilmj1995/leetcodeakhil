class Solution:
    def isHappy(self, n: int) -> bool:
        array=[]
        while True:
           k=0
           for i in str(n):
             k+=int(i)**2
             print(k)
           if k==1:
              return True
           if k in array:
             return False
           array.append(k)
           n=k


