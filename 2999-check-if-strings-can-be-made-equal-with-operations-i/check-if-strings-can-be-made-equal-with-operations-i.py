class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        count=0
        if s1==s2:
            return True
        for i in range(len(s1)):
            for j in range(len(s2)):
                if j-i==2 and s1[i]==s2[j]:
                   s1[i],s1[j]=s1[j],s1[i]
                   if s1==s2:
                      return True
                
            


        return False              
        
        
                    



                

