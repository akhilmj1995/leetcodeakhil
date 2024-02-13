class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        a=[]
        for i in grid:
            m=0
            for j in i:
                if j==1:
                    m+=1
            a.append(m)
        print(a)
        return a.index(max(a))
        
                
            
    