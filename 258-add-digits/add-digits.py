class Solution:
    def addDigits(self, num: int) -> int:
        a=num
        while len(str(a))>1:
            sum=0
            for i in str(a):
                sum+=int(i)
            a=sum
        return a

            
