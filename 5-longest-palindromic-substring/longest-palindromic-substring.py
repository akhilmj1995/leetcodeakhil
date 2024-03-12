class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=str()
        if len(s)==1 or len(set(s))==1:
            return s
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                a=s[i:j+1]
                if a==a[::-1] and len(a)>len(m):
                    m=s[i:j+1]
        if len(m)==0:
            return s[0]
        return m
                    