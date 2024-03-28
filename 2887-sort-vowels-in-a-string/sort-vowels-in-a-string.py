class Solution:
    def sortVowels(self, s: str) -> str:
        listvo={'A','E','I','O','U','a','e','i','o','u'}
        listnew=list()
        for i in s:
            if i in listvo:
                listnew+=i
        listnew.sort()
        t=str()
        k=0
        for i in s:
            if i in listvo:
                t+=listnew[k]
                k+=1
            else:
                t+=i
        return t

