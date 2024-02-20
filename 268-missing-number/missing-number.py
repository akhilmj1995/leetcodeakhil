class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sumorg=n*(n+1)//2
        sumarr=sum(nums)
        return sumorg-sumarr