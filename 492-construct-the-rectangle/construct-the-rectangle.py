class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        return next([area//b,b] for b in range(int(area**0.5),0,-1) if area%b==0 )
        


            

            
