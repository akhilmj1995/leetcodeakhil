class Solution:
    def isHappy(self, n: int) -> bool:
        m=str(n)
        array=[]
        while True:
            sum=0
            for i in m:
                sum+=int(i)**2
            if sum in array:
                return False
            array.append(sum)
            if sum==1:
                return True
            m=str(sum)
        return False
        
    
        