class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        first=list(s)
        second=list(t)
        val=str()
        for i in second:
            if i in first:
                first.remove(i)
                continue
            val+=i
        return val
            
            
        
            