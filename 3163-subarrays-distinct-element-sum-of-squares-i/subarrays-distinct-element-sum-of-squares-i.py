class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
               b=nums[i:j+1]
               a=len(set(b))
               sum+=a*a
        return sum
