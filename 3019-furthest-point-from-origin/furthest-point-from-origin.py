class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a=0
        if moves.count('L')<=moves.count('R'):
            moves=moves.replace('_','R')
        else:
            moves=moves.replace('_','L')
        print(moves)
        for i in range(len(moves)):
            if moves[i]=="L":
                a-=1
            if moves[i]=='R':
                a+=1
        return abs(a) 

            
           
        
                
               

        