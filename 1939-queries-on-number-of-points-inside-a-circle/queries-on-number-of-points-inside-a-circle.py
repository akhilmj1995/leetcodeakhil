class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        k=list()
        for i in queries:
            m=0
            for j in points:
                if ((j[0]-i[0])**2+(j[1]-i[1])**2)<=(i[2]**2):
                    m+=1
            k.append(m)
        return k
