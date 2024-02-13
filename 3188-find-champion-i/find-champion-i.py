class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        a=[sum(i) for i in grid]
        return a.index(max(a))
        
                
            
    