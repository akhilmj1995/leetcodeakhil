class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a=str()
        ones=s.count('1')-1
        zero=len(s)-ones
        for i in range(len(s)-1):
            if ones>0:
                a+='1'
                ones-=1
            else:
                a+='0'
        a+='1'
        return a
            
         



         
         


