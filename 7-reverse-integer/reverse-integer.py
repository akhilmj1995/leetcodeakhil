class Solution:
    def reverse(self, x: int) -> int:
        a=str(x)
        a=a.replace('-','')
        a=a[::-1]
        if int(a)<=pow(-2,31):
            return 0     
        if int(a)>=pow(2,31):
            return 0
        if x<0:
            b=int(a)*-1
        else:
            b=int(a)
        return b
        