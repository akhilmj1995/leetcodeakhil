class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
       n=len(grid)**2
       orgsum=n*(n+1)//2
       actsum=sum([sum(x) for x in grid])
       main=[]
       for i in grid:
           for j in i:
               main.append(j)
       for i in main:
           if main.count(i)!=1:
               a=i
               break
       b=[]
       miss=orgsum-actsum+a
       b.append(a)
       b.append(miss)
       return b




           


        
           
           
        