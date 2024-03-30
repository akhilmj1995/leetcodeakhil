class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m=list(s)
        n=list(t)
        m.sort()
        n.sort()
        if m==n:     
            return True
        return False