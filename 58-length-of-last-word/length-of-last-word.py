class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s=s[::-1]
        s=s.strip()
        for i in s:
            if i==" ":
                break
            else:
                count+=1
        return count