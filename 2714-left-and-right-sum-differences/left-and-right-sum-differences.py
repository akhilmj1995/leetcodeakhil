class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre=0
        aft=sum(nums)
        ans=[]
        for i in nums:
            pre+=i
            ans.append(abs(pre-aft))
            aft-=i
        return ans

