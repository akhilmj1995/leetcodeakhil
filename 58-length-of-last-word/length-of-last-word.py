class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s.strip()
        for i in s[::-1]:
            if i==" ":
                break
            count+=1
        return count