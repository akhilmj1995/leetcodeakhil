class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        k=len(candyType)//2
        if k>len(set(candyType)):
           return len(set(candyType))
        return k