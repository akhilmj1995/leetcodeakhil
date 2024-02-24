class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            k=sum(nums[:i])-sum(nums[i+1:])
            ans.append(abs(k))
        return ans

