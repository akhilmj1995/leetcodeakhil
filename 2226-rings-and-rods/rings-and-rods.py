class Solution:
    def countPoints(self, rings: str) -> int:
        r=[]
        b=[]
        g=[]
        c=0
        for i in range(len(rings)):
            if rings[i]=='B':
                b.append(int(rings[i+1]))
            elif rings[i]=='R':
                r.append(int(rings[i+1]))
            elif rings[i]=='G':
                g.append(int(rings[i+1]))
            else:
                continue
        
        r=set(r)
        print(r,g,b)
        for i in r:
            if i in g and i in b:
                c+=1
        return c
                
                 
                
              


