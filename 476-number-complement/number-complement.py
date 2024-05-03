class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num).replace("0b", "")
        k=str()
        for i in a:
            if i=='0':
                k+='1'
            else:
                k+='0'
        k=int(k,2)
        return k
            
        