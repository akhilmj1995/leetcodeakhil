class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t) or set(s)!=set(t):
            return False
        m=list(s)
        n=list(t)
        m.sort()
        n.sort()
        if m==n:     
            return True
        return False