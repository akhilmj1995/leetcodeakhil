class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        countone=0
        counttwo=0
        for i in range(0,int(len(s)/2)):
            if s[i] in vowels:
                countone+=1
        for i in range(int(len(s)/2),len(s)):
            if s[i] in vowels:
                counttwo+=1
        if countone==counttwo :
             return True
        return False