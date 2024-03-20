class Solution:
    def addDigits(self, num: int) -> int:
        a=num
        if len(str(a))==1:
            return a
        while len(str(a))>1:
            sum=0
            for i in str(a):
                sum+=int(i)
            a=sum
        return a

            
