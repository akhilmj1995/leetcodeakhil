class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=str()
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i]
        a=a.casefold()
        print(a)
        if a==a[::-1]:
            return True
        else:
            return False


