class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=[]
        b=[]
        if len(trust)==0 and n==1:
            return n
        if len(trust)==0:
            return -1
        for i in trust:
             b.append(i[0])
             a.append(i[1])
        for i in set(a):
            if i not in b and a.count(i)==n-1:
                return i
        return -1



