class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a=[]
        b=set(arr)
        b=list(b)
        for i in b:
            a.append(arr.count(i))
        print(a)
        for i in a:
            if a.count(i)!=1 :
                return False
        return True
        
        