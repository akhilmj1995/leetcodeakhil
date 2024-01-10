class Solution:
    def romanToInt(self, s: str) -> int:
        sol={
             "I":1,
             "V":5,
             "X":10,
             "L":50,
             "C":100,
             "D":500,
             "M":1000
            }
        i=len(s)-1
        N=len(s)
        count=0
        while i>=0:
            if i<N-1 and sol[s[i]]<sol[s[i+1]]:
                count-=sol[s[i]]
            else:
                count+=sol[s[i]]
            i-=1
        return count
     