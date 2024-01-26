class Solution:
    def finalString(self, s: str) -> str:
        a=str()
        for k in range(len(s)):
            if s[k]=='i':
                a=a[k-1::-1]
            else:
                a+=s[k]
        return a       
        