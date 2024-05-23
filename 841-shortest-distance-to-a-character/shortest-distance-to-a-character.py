class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        arr=list()
        out=list()
        for i in range(len(s)):
            if s[i]==c:
                arr.append(i)
        print(arr)
        for i in range(len(s)):
            mini=list()
            for j in arr:
                mini.append(abs(i-j))
            out.append(min(mini))
        return out
            

              
