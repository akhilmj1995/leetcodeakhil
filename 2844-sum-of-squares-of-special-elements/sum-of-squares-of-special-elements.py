class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        a=0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0:
                a+=nums[i]**2
        return a
        