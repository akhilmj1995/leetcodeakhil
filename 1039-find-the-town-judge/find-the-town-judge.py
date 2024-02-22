class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a=[]
        b=[]
        if trust==[]:
            return n if n==1 else -1
        for i in trust:
             b.append(i[0])
             a.append(i[1])
        for i in set(a):
            if i not in b and a.count(i)==n-1:
                return i
        return -1



