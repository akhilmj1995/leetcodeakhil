class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
       if len(set(s))!=len(set(t)):
          return False
       k=dict()
       m=str()
       for i in range(len(s)):
            try :
                k.update({s[i]:t[i]})
            except :
                return False
       for i in s:
           m+=k[i]
       print(m)
       print(t)
       if m==t:
         return True
       return False
       