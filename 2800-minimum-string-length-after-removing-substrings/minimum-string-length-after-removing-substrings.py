class Solution:
    def minLength(self, s: str) -> int:
        count=len(s)
        while ('AB' in s or 'CD' in s):
           s=s.replace("AB",'')
           s=s.replace("CD","")
        print(s)
        return len(s)
           

            
         
        
    
