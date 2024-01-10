class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best=0
        i=1
        while True:
            b=('0'*i)+('1'*i)
            if b not in s:
                break
            best=i
            i+=1
        return best*2

          

