class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        sub=["--X","X--"]
        add=["X++","++X"]
        for i in operations:
            if i in sub:
                x-=1
            if i in add:
                x+=1
        return x
