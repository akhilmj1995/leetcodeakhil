class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        for i in range(len(digits)):
            sum=sum*10+digits[i]
        sum=sum+1
        sum=str(sum)
        a=[]
        for i in sum:
            a.append(int(i))
        return a